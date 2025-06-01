from DTOs.MovieDto import MovieData
from repositories.movies.Movies import MoviesRepository

class MovieSave:

    def __init__(self, movieData: MovieData):
        self.movieData = movieData

    def save(self):
        moviesRepository = MoviesRepository(self.movieData)
        moviesRepository.save()