from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session


def add_genre(session: Session):
    name = input("Enter new genre (or 0 to cancel): ").strip()

    if name == "0":
        print("Cancelled.")
        return

    new_genre = Genres(genre = name)
    session.add(new_genre)
    session.commit()
    print(f"'{name}' added as a genre.")

def list_genres(session: Session):
    genres = session.query(Genres).all()
    print("\nGenres:")
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

    new_name = input(f"New name for '{genre.genre}' (leave blank to keep): ").strip()

    if new_name:
        genre.genre = new_name
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
        print("Cancelled.")
        return

    genre = session.query(Genres).filter_by(genre_id=genre_id).first()

    confirm = input(f"Are you sure you want to delete '{genre.genre}'? (y/N): ").strip().lower()
    if confirm == 'y':
        session.delete(genre)
        session.commit()
        print("Genre deleted.")
    else:
        print("Cancelled.")
