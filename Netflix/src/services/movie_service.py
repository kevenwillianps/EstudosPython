from time import sleep
from src.dtos.movie_dto import MovieDto
from src.actions.movies.delete_movie_action import DeleteMovieAction
from src.actions.movies.save_movie_action import SaveMovieAction
from src.actions.movies.log_movie_action import LogMovieAction

""" Classe responsável por instânciar os actions necessário para realizar o procedimento desejado """
class MovieService:

    """ Injeção de depêndencias dos dados do filme """
    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto

    """ Método responsável por executar a action de salvar o registro """
    def save(self):

        # Registra um novo filme
        saveMovieAction = SaveMovieAction(self.movieDto)
        saveMovieAction.save()

        # Registra um novo log
        logMovieAction = LogMovieAction(self.movieDto)
        logMovieAction.save()
        sleep(1)

    """ Método responsável por executar a action de remover o registro """
    def delete(self):

        # Registra um novo filme
        deleteMovieAction = DeleteMovieAction(self.movieDto)
        deleteMovieAction.save()

        # Registra um novo log
        logMovieAction = LogMovieAction(self.movieDto)
        logMovieAction.save()
        sleep(1)