from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session




def add_author( session: Session ):
    name = input( "Enter new author name (or 0 to cancel): ").strip()

    if name == "0":
        print( "Cancelled.")
        return

    new_author = Authors( name = name)
    session.add( new_author)
    session.commit()
    print(f"'{name}' added.")


def list_authors(session: Session):
    authors = session.query(Authors).all()
    print("\nAuthors:")
    for author in authors:
        print(f"{author.author_id}. {author.name}")


def update_author(session: Session):
    list_authors(session)

    try:
        author_id = int(input("Enter author ID to update (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return

    if author_id == 0:
        print("Cancelled.")
        return

    author = session.query(Authors).filter_by(author_id=author_id).first()

    new_name = input(f"New name for '{author.name}' (leave blank to keep): ").strip()

    if new_name:
        author.name = new_name
        session.commit()
        print("Author updated.")
    else:
        print("No changes made.")

def delete_author(session: Session):
    list_authors(session)

    try:
        author_id = int(input("Enter author ID to delete (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return

    if author_id == 0:
        print("Cancelled.")
        return

    author = session.query(Authors).filter_by(author_id=author_id).first()

    confirm = input(f"Are you sure you want to delete '{author.name}'? (y/N): ").strip().lower()
    if confirm == 'y':
        session.delete(author)
        session.commit()
        print("Author deleted.")
    else:
        print("Cancelled.")

