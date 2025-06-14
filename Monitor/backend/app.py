from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import threading
import time
import psutil
import os

app = Flask(__name__, static_folder="../frontend")
socketio = SocketIO(app, cors_allowed_origins="*")

def format_bytes(size):
    # função auxiliar para formatar tamanhos em MB/GB
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def collect_data():
    boot_time = psutil.boot_time()
    while True:
        cpu_freq = psutil.cpu_freq()
        virtual_mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        data = {
            "cpu": {
                "percent": psutil.cpu_percent(),
                "cores": psutil.cpu_count(logical=True),
                "freq_current": cpu_freq.current,
                "freq_max": cpu_freq.max
            },
            "memory": {
                "percent": virtual_mem.percent,
                "total": format_bytes(virtual_mem.total),
                "used": format_bytes(virtual_mem.used),
                "available": format_bytes(virtual_mem.available)
            },
            "disk": {
                "percent": disk.percent,
                "total": format_bytes(disk.total),
                "used": format_bytes(disk.used),
                "free": format_bytes(disk.free)
            },
            "uptime": time.time() - boot_time
        }
        socketio.emit('update', data)
        time.sleep(1)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    thread = threading.Thread(target=collect_data)
    thread.daemon = True
    thread.start()
    socketio.run(app, host="0.0.0.0", port=5000)
