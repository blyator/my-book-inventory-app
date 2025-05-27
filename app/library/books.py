from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session
import os

def add_book( session: Session ):
    title = input(  "New title ( Enter 0 to cancel): ").strip()
    if title == "0":
        print( "Cancelled." )
        return

    os.system( "clear" )
    print( "****************** Add an Author ************************")

    authors = session.query( Authors ).all()

    while True:
        print( "\n0. Cancel")
        print( "1.Add a new author" )
        print( "\nSelect from existing authors:")

        for index, author in enumerate( authors, start=2 ):
            print( f"{index}. {author.name}" )

        try:
            user_choice = int( input("Enter your choice: "))
        except ValueError:
            print( "Invalid Choice")
            continue

        if user_choice == 0:
            print( "Cancelled.")
            return

        elif user_choice == 1:
            os.system("clear")
            new_author_name = input( "Enter new author name: " ).strip()
            if not new_author_name:
                print( "Name cannot be empty." )
                continue
            new_author = Authors( name=new_author_name )
            session.add( new_author )
            session.commit()
            author_id = new_author.author_id
            break

        else:
            try:
                author_id = authors[user_choice - 2].author_id
                break
            except IndexError:
                print( "Invalid author.please try again")
                continue

    os.system("clear")

    genres = session.query( Genres ).all()

    while True:
        print( "\n****************** Select a Genre ************************")
        print( "0. Cancel" )
        print( "1.Add new genre" )
        print( "\nChoose from existing genres:")

        for index, genre in enumerate( genres, start=2 ):
            print( f"{index}. {genre.genre}" )

        try:
            user_choice = int( input("Enter your choice: "))
        except ValueError:
            print( "Invalid choice")
            continue

        if user_choice == 0:
            print( "Cancelled.")
            return

        elif user_choice == 1:
            os.system("clear")
            new_genre_name = input( "Enter new genre name: " ).strip()
            new_genre = Genres( genre = new_genre_name )
            session.add( new_genre )
            session.commit()
            genre_id = new_genre.genre_id
            break

        else:
            try:
                genre_id = genres[user_choice - 2].genre_id
                break
            except IndexError:
                print( "Invalid genre. please try again.")
                continue


    new_book = Books( title=title, author_id=author_id, genre_id=genre_id )
    session.add( new_book )
    session.commit()
    os.system("clear")
    print( f"\n'{title}' as been added to your book inventory." )


def get_books (session: Session ):
    books = session.query( Books ).all()
    print( "\nBooks in inventory:" )
    for book in books:
        author = session.query( Authors ).filter_by( author_id=book.author_id ).first()
        genre = session.query( Genres ).filter_by( genre_id=book.genre_id ).first()
        print( f"{book.book_id}. {book.title}, Author: {author.name if author else 'Unknown'}, Genre: {genre.genre if genre else 'Unknown'}" )


def book_by_title(session: Session, title: str):
    books = session.query(Books).filter(Books.title.ilike(f"%{title}%")).all()

    if not books:
        print("No books found.")
        return None

    os.system("clear")

    print(f"\nSearch Results for '{title}`\n")

    results = []
    for book in books:
        author = session.query(Authors).filter_by(author_id=book.author_id).first()
        genre = session.query(Genres).filter_by(genre_id=book.genre_id).first()

        result = {
            "title": book.title,
            "author": author.name if author else "Unknown",
            "genre": genre.genre if genre else "Unknown"
        }
        results.append(result)

        print(f"Title : {result['title']}")
        print(f"Author: {result['author']}")
        print(f"Genre : {result['genre']}\n")

    return results


def delete_book( session: Session ):
    books = session.query( Books ).all()

    if not books:
        print( "No books available to delete.")
        return

    while True:
        print("\nSelect a book to delete:")
        for book in books:
            print( f"{book.book_id}. {book.title}")
        print( "0. Cancel" )

        try:
            choice = int(input("Enter the book ID to delete: "))
        except ValueError:
            print( "Invalid input. Please enter a valid number.")
            continue

        if choice == 0:
            print( "Deletion cancelled." )
            return

        book_to_delete = session.query( Books ).filter_by( book_id = choice ).first()

        if not book_to_delete:
            print( "Book not found. Please enter a valid book ID.")
            continue

        session.delete( book_to_delete )
        session.commit()
        print( f"Book '{book_to_delete.title}' deleted successfully.")
        break


def update_book( session: Session ):
    books = session.query( Books ).all()

    print( "\nYour Books:" )
    for book in books:
        print( f"{book.book_id}. {book.title}" )

    try:
        choice = int( input("Choose a book to update (pick ID, or 0 to cancel): "))
    except ValueError:
        print( "Invalid input." )
        return

    if choice == 0:
        print( "Update cancelled." )
        return

    book = session.query( Books ).filter_by( book_id=choice ).first()
    os.system("clear")

    new_title = input(f"New book title (leave blank to keep '{book.title}'): ").strip()
    if new_title:
        book.title = new_title

    author = session.query( Authors ).filter_by( author_id=book.author_id ).first()
    if author:
        new_author = input(f"New author name (leave blank to keep '{author.name}'): ").strip()
        if new_author:
            author.name = new_author

    genre = session.query(Genres).filter_by(genre_id=book.genre_id).first()
    if genre:
        new_genre = input(f"New genre name (leave blank to keep '{genre.genre}'): ").strip()
        if new_genre:
            genre.genre = new_genre
            
    os.system("clear")

    session.commit()
    print(f"'{book.title}' updated.")


def delete_book(session: Session):
    books = session.query(Books).all()

    print("\nYour Books:")
    for book in books:
        print(f"{book.book_id}. {book.title}")

    choice = int(input("Choose a book to delete (pick ID, or 0 to cancel): "))

    if choice == 0:
        print("Cancelled.")
        return

    book = session.query(Books).filter_by(book_id=choice).first()
    if not book:
        print("Book not found.")
        return
    
    os.system("clear")

    confirm = input(f"Are you sure you want to delete `{book.title}` ? (y/N): ").strip().lower()
    if confirm == 'y':
        os.system("clear")
        session.delete(book)
        session.commit()
        print(f"'{book.title}' deleted.")
    else:
        print("Cancelled.")
