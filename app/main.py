from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from library.authors import create_author
from library.books import add_book
from library.genres import create_genre

engine = create_engine("sqlite:///app/db/books.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Example usage:
# create_author(session)
add_book(session)
# create_genre(session)
