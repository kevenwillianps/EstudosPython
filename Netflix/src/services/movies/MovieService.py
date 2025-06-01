from time import sleep

from DTOs.MovieDto import MovieData
from actions.movies.MovieSave import MovieSave
from actions.movies.MovieLog import MovieLog
from actions.movies.MovieDelete import MovieDelete

class MovieService:

    # função executada quando a classe é instância
    # Essa função espera valores do tipo MovieData
    def __init__(self, movieData: MovieData):
        self.movieData = movieData

    # Função para executa a action de salvar os dados
    def save(self):

        # Registra um novo filme
        movieSave = MovieSave(self.movieData)
        movieSave.save()

        # Registra um novo log
        movieLog = MovieLog(self.movieData)
        movieLog.save()
        sleep(1)

    def delete(self):

        # Realiza a remoção do registro
        movieDelete = MovieDelete(self.movieData)
        movieDelete.delete()

        # Registra um novo log
        movieLog = MovieLog(self.movieData)
        movieLog.save()
        sleep(1)