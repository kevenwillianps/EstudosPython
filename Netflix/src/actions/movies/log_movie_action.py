from src.dtos.movie_dto import MovieDto

class LogMovieAction:

    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto

    def save(self):
        print(f"Executando log: {self.movieDto}")