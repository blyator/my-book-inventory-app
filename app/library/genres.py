from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session
import os


def add_genre(session):
    genre_name = input("Enter new genre: ").strip()


    existing_genre = session.query(Genres).filter(Genres.genre.ilike(genre_name)).first()

    if existing_genre:
        print(f"'{genre_name}' already exists.")
        return

    new_genre = Genres(genre=genre_name)
    session.add(new_genre)
    session.commit()
    os.system("clear")
    print(f"'{genre_name}' added to genres.")


def list_genres(session: Session):
    genres = session.query(Genres).all()
    print("Current genres:")
    for genre in genres:
        print(f"{genre.genre_id}. {genre.genre}")


def update_genre(session: Session):
    list_genres(session)
    
    try:
        genre_id = int(input("Enter genre ID to update (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return

    if genre_id == 0:
        print("Cancelled.")
        return

    genre = session.query(Genres).filter_by(genre_id=genre_id).first()

    os.system("clear")
    
    if not genre:
        print(f"No genre found.")
        return
    

    new_name = input(f"New name for '{genre.genre}' (leave blank to keep): ").strip()

    os.system("clear")

    if new_name:
        genre.name = new_name
        session.commit()
        print("Genre updated.")
    else:
        print("No changes made.")


def delete_genre(session: Session):
    list_genres(session)

    try:
        genre_id = int(input("Enter genre ID to delete (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return
    if genre_id == 0:
        os.system("clear")
        print("Cancelled.")
        return

    genre = session.query(Genres).filter_by(genre_id=genre_id).first()

    os.system("clear")

    if not genre:
        print("No genre found.")
        return

    confirm = input(f"Are you sure you want to delete '{genre.genre}'? (Y/n): ").strip().lower()
    if confirm == 'y':
        os.system("clear")
        session.delete(genre)
        session.commit()
        print("Genre deleted.")
    else:
        print("Cancelled.")


def genre_by_name(session: Session, genre_name: str):
    genres = session.query(Genres).filter(Genres.genre.ilike(f"%{genre_name}%")).all()

    if not genres:
        print("No genres found.")
        return None

    os.system("clear")

    print(f"\nSearch Results for '{genre_name}'\n")

    results = []

    for genre in genres:

        total_books = session.query(Books).filter_by(genre_id=genre.genre_id).count()

        result = {
            "genre": genre.genre,
            "total_books": total_books
        }
        results.append(result)

        print(f"Genre : {result['genre']}")
        print(f"Books : {result['total_books']}\n")

    return results
