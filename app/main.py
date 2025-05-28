from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from library.genres import add_genre, delete_genre, update_genre, list_genres, genre_by_name
from library.authors import add_author, delete_author, update_author, list_authors, author_by_name
from library.books import add_book, delete_book, update_book, get_books, book_by_title
import os

engine = create_engine("sqlite:///app/db/books.sqlite")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def manage_books():
    while True:
        print("\n********** Book Management **********")
        print("\n1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Back to Main Menu")

        choice = input("\nChoose an option: ")

        if choice == '1':
            os.system("clear")
            add_book(session)
        elif choice == '2':
            os.system("clear")
            get_books(session)
        elif choice == '3':
            os.system("clear")
            title = input("Book title: ")
            book_by_title(session, title)
        elif choice == '4':
            os.system("clear")
            update_book(session)
        elif choice == '5':
            os.system("clear")
            delete_book(session)
        elif choice == '6':
            os.system("clear")
            break
        else:
            print("Invalid choice, please try again.")

def manage_authors():
    while True:
        print("\n********** Author Management **********")
        print("\n1. Add Author")
        print("2. List Authors")
        print("3. Search Author")
        print("4. Update Author")
        print("5. Delete Author")
        print("6. Back to Main Menu")

        choice = input("\nChoose an option: ")
        os.system("clear")

        if choice == '1':
            add_author(session)
        elif choice == '2':
            list_authors(session)
        elif choice == '3':
            name = input("Name of Author: ")
            author_by_name(session, name)
        elif choice == '4':
            update_author(session)
        elif choice == '5':
            delete_author(session)
        elif choice == '6':
            os.system("clear")
            break
        else:
            print("Invalid choice, please try again.")

def manage_genres():
    while True:
        print("\n********** Genre Management **********")
        print("\n1. Add Genre")
        print("2. List Genres")
        print("3. Search Genre")
        print("4. Update Genre")
        print("5. Delete Genre")
        print("6. Back to Main Menu")

        choice = input("\nChoose an option: ")
        os.system("clear")

        if choice == '1':
            add_genre(session)
        elif choice == '2':
            list_genres(session)
        elif choice == '3':
            genre = input("Genre name: ")
            genre_by_name(session, genre)
        elif choice == '4':
            update_genre(session)
        elif choice == '5':
            delete_genre(session)
        elif choice == '6':
            os.system("clear")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\n********** My Book Inventory **********")
        print("\nWhat would you like to do?")
        print("\n1. Manage Books")
        print("2. Manage Authors")
        print("3. Manage Genres")
        print("4. Exit")

        choice = input("\nChoose an option: ")
        os.system("clear")

        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_authors()
        elif choice == '3':
            manage_genres()
        elif choice == '4':
            print("Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")

main()