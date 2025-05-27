import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Books, Authors, Genres


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "books.db")
engine = create_engine(f"sqlite:///{db_path}")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


def get_or_create_author(name):
    author = session.query(Authors).filter_by(name=name).first()
    if not author:
        author = Authors(name=name)
        session.add(author)
        session.commit()
    return author

def get_or_create_genre(name):
    genre = session.query(Genres).filter(Genres.genre.ilike(name)).first()
    if not genre:
        genre = Genres(genre=name)
        session.add(genre)
        session.commit()
    return genre

def add_book(title, author_name, genre_name="Fiction"):
    author = get_or_create_author(author_name)
    genre = get_or_create_genre(genre_name)
    exists = session.query(Books).filter(Books.title.ilike(title)).first()
    if not exists:
        book = Books(title=title, author_id=author.author_id, genre_id=genre.genre_id)
        session.add(book)

# Book data
books_data = [
    ("My Life in Crime", "John Kiriamiti", "Crime"),
    ("My Life with a Criminal", "John Kiriamiti", "Crime"),
    ("Son of Fate", "John Kiriamiti", "fiction"),

    ("Across the Bridge", "Meja Mwangi", "Fiction"),
    ("Three Days on the Cross", "Meja Mwangi", "Fiction"),

    ("Circling the Sun", "Paula McLain", "Historical Fiction"),
    ("Captured by Raiders", "Grace Ogot", "Historical Fiction"),

    ("Weep Not, Child", "Ngũgĩ wa Thiong'o", "Novel"),
    ("A Grain of Wheat", "Ngũgĩ wa Thiong'o", "Novel"),
    ("The River Between", "Ngũgĩ wa Thiong'o", "Novel"),

    ("Doctor at Heart", "Dr. Gikonyo", "Medical Fiction"),
    ("Not Yet Uhuru", "Jomo Kenyatta", "Biography"),

    ("Cross", "James Patterson", "Thriller"),
    ("Eruption", "James Patterson", "Thriller"),
    ("Kiss the Girls", "James Patterson", "Thriller"),

    ("Fifty Shades of Grey", "E. L. James", "Romance"),
    ("Fifty Shades Darker", "E. L. James", "Romance"),

    ("Book of Lovers", "Emily Henry", "Romance"),
    ("Bad Behavior", "Adrianne Finlay", "Erotica"),
]


for entry in books_data:
    if len(entry) == 3:
        title, author, genre = entry
        add_book(title, author, genre)
    else:
        title, author = entry
        add_book(title, author)

session.commit()
print("books database seeded successfully.")
