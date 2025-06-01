from DTOs.MovieDto import MovieData
from services.movies.MovieService import MovieService

class MoviesController:

    # Classe para salvar um novo filme
    def save(self, name: str, year: int) -> None:

        # Preenche o DTO para transferir entre as camadas
        movieData = MovieData(
            title=name,
            year=year
        )

        # Instância a classe service, que funciona como classe intermediária
        # Em seguida registra os dados em banco de dados
        movieService = MovieService(movieData)
        movieService.save()

    # Método para remover determinado registro
    def delete(self, name: str) -> None:

        #preenche o DTO para transportar entre as camadas
        movieData = MovieData(
            title=name,
            year=None
        )

        # Instância a classe services, que opera como classe intermediária
        # Em seguida remove o registro informado
        movieService = MovieService(movieData)
        movieService.delete()