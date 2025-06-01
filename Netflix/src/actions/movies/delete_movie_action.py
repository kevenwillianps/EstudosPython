from src.dtos.movie_dto import MovieDto

class DeleteMovieAction:

    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto

    def delete(self):
        # Lógica a ser executada
        # Mensagem simbolica
        print(f"Removendo o registro: {self.movieDto.title}")