# Importação para trabalhar com Dtos
from dataclasses import dataclass

@dataclass
class MovieDto:
    title: str
    year: int