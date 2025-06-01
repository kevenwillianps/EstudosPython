from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from src.dtos.movie_dto import MovieDto

class MovieRepository:

    def __init__(self, movieDto: MovieDto):
        self.movieDto = movieDto
        self.engine = create_engine("sqlite:///meubanco.db", echo=True)

        # Metadados e tabela
        self.metadata = MetaData()
        self.filmes = Table(
            "filmes",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String, nullable=False),
            Column("year", String, nullable=False),
        )

        # Cria a tabela se não existir
        self.metadata.create_all(self.engine)

    def save(self):
        with self.engine.connect() as conn:
            conn.execute(
                text("INSERT INTO filmes (name, year) VALUES (:name, :year)"),
                {
                    "name": self.movieDto.title,
                    "year": self.movieDto.year
                }
            )
            conn.commit()