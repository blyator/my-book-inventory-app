from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session
import os

def add_book(session: Session):
    title = input("Enter book title (Enter 0 to cancel): ").strip()
    if title == "0":
        print("Book creation cancelled.")
        return

    os.system("clear")
    print("****************** Add an Author ************************")

    authors = session.query(Authors).all()

    while True:
        print("\n0. Cancel")
        print("1.Add a new author")
        print("\nSelect from existing authors:")

        for index, author in enumerate(authors, start=2):
            print(f"{index}. {author.name}")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice")
            continue

        if user_choice == 0:
            print("Book creation cancelled.")
            return

        elif user_choice == 1:
            new_author_name = input("Enter new author name: ").strip()
            if not new_author_name:
                print("Name cannot be empty.")
                continue
            new_author = Authors(name=new_author_name)
            session.add(new_author)
            session.commit()
            author_id = new_author.author_id
            break

        else:
            try:
                author_id = authors[user_choice - 2].author_id
                break
            except IndexError:
                print("Invalid author selection.")
                continue

    os.system("clear")

    genres = session.query(Genres).all()

    while True:
        print("\n****************** Select a Genre ************************")
        print("0. Cancel")
        print("1.Add New Genre")
        print("\nSelect from existing genres:")

        for index, genre in enumerate(genres, start=2):
            print(f"{index}. {genre.genre}")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input")
            continue

        if user_choice == 0:
            print("Book creation cancelled.")
            return

        elif user_choice == 1:
            new_genre_name = input("Enter new genre name: ").strip()
            new_genre = Genres( genre = new_genre_name )
            session.add(new_genre)
            session.commit()
            genre_id = new_genre.genre_id
            break

        else:
            try:
                genre_id = genres[user_choice - 2].genre_id
                break
            except IndexError:
                print("Invalid genre selection. please try again.")
                continue


    new_book = Books(title=title, author_id=author_id, genre_id=genre_id)
    session.add(new_book)
    session.commit()
    print(f"\nSuccess! Book '{title}' added to inventory.")
