from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session




def create_author(session: Session):
    name = input("Enter author name: ")
    author = Authors(name=name)
    session.add(author)
    session.commit()
    print(f"Author '{name}' created successfully.")
