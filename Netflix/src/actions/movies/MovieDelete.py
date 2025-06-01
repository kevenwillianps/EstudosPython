from DTOs.MovieDto import MovieData

class MovieDelete:

    def __init__(self, movieData: MovieData):
        self.movieData = movieData

    def delete(self):
        # Lógica a ser executada
        # Mensagem simbolica
        print(f"Removendo o registro: {self.movieData.title}")