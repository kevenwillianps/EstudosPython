from src.dtos.movie_dto import MovieDto

""" Classe responsavel por gerar logs em tela dos dados que estão sendo persistidos em banco de dados """
class LogMovieAction:

    """ Inicializa os dados do log com o Dto informado """
    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto

    """ Executa o registro de log """
    def execute(self):
        print(f"Executando log: {self.movieDto}")