# Importação para trabalhar com Dtos
from dataclasses import dataclass

@dataclass
class MovieData:
    title: str
    year: int