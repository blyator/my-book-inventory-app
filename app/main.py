from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from library.authors import create_author
from library.books import add_book, delete_book, update_book, delete_book
from library.books import get_books
from library.genres import create_genre
from library.books import book_by_title

engine = create_engine("sqlite:///app/db/books.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Example usage:
# create_author(session)
add_book(session)
# create_genre(session)
#get_books(session)
#book_by_title(session, "wily")
#delete_book(session, 1)  # Replace 1 with the actual book_id you want to delete
#update_book(session)  # Replace 1 with the actual book_id you want to update
#delete_book(session)  # Uncomment to delete a book
