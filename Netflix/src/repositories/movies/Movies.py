from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from DTOs.MovieDto import MovieData

class MoviesRepository:

    def __init__(self, movieData: MovieData):
        self.movieData = movieData
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
                    "name": self.movieData.title,
                    "year": self.movieData.year
                }
            )
            conn.commit()
