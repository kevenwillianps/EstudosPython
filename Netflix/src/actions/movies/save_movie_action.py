from src.dtos.movie_dto import MovieDto
from src.repositories.movie_repository import MovieRepository

""" Classe responsável por conectar o repositório """
class SaveMovieAction:

    """ Injeção de depêndencias dos dados do filme """
    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto

    """ Método responsável por executar registrar os dados do filme """
    def save(self):

        # Mensagem de andamento
        print(f"Registrando filme...")

        # Instânciamento do repositório
        movieRepository = MovieRepository(self.movieDto)

        # Executa o método de salvar
        movieRepository.save()