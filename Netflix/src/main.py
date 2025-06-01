# Importação de classes
from controllers.movies.MovieController import MoviesController

# Instânciamento da classe de filme
movieController = MoviesController()

# Regsitra um novo filme no catalogo
print(movieController.save('Exterminador do Futuro: A rebelião das Máquinas', 2025))