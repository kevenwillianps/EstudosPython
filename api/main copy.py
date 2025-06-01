# Importação do FastApi
from fastapi import FastAPI;

# Cria uma instãncia do FastAPI
# e define o nome da aplicação
app = FastAPI();

# Criar uma banco de dados fake
items = {
    1 : {"name": "Item 1", "price": 10.0},
    2 : {"name": "Item 2", "price": 10.0},
    2 : {"name": "Item 3", "price": 10.0}
}

# Endpoint padrão e para retornar todos os itens
@app.get("/")
def all():
    return items;

# Endpoint para retornar um item especifico
# O id é passado como parâmetro na url
@app.get("/item/{id}")
def get(id : int):
    # Verificar se o id esta na lista de itens
    if id in items:
        # Retornar o item solicitado
        return items[id]
    # SE o id não estiver na lista de itens
    else:
        # Retornar uma mensagem de erro
        return {"Item não encontrado!" : id}