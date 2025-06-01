# Importação de classes
from src.controllers.movie_controller import MoviesController

def main():

    # Instânciamento da classe de filme
    movieController = MoviesController()

    # Registra um novo filme no catálogo
    movieController.save('Avatar: Caminho da Água', 2025)