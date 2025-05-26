from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session


def create_genre(session: Session):
    genre = input("Enter genre: ")
    genre_name = Genres(genre = genre)
    session.add(genre_name)
    session.commit()
    print(f"Genre {genre} created successfully.")