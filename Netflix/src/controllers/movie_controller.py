# Importação de classes
from src.dtos.movie_dto import MovieDto
from src.services.movie_service import MovieService

""" Classe responsavel por controlar as entradas e saídas solicitadas"""
class MoviesController:

    """ Método para salvar um novo registro """
    def save(self, name: str, year: int) -> None:

        # Mensagem de andamento
        print(f"Preparando registro...")

        # Preenche o DTO para transferir entre as camadas
        movieDto = MovieDto(
            title=name,
            year=year
        )

        # Instância a classe service, que funciona como classe intermediária
        # Em seguida registra os dados em banco de dados
        movieService = MovieService(movieDto)
        movieService.save()

    """ Método para remover um determinado registro """
    def delete(self, name: str) -> None:

        #preenche o DTO para transportar entre as camadas
        movieDto = MovieDto(
            title=name,
            year=None
        )

        # Instância a classe services, que opera como classe intermediária
        # Em seguida remove o registro informado
        movieService = MovieService(movieDto)
        movieService.delete()