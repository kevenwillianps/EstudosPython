from DTOs.MovieDto import MovieData

class MovieLog:

    def __init__(self, movieData : MovieData):
        self.movieData = movieData

    def save(self):
        print(f"Executando log: {self.movieData}")