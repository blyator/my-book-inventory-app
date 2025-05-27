from db.models import Authors, Genres, Books
from sqlalchemy.orm import Session
import os




def add_author( session: Session ):
    name = input( "Enter new author name (or 0 to cancel): ").strip()

    os.system("clear")

    if name == "0":
        os.system("clear")
        print( "Cancelled.")
        return

    new_author = Authors( name = name)
    session.add( new_author)
    session.commit()
    print(f"Author '{name}' added.")


def list_authors(session: Session):
    authors = session.query(Authors).all()
    print("Authors in Inventory:\n")
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
        os.system("clear")
        print("Cancelled.")
        return

    author = session.query(Authors).filter_by(author_id=author_id).first()

    os.system("clear")

    new_name = input(f"New name for '{author.name}' (leave blank to keep): ").strip()

    os.system("clear")

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

    os.system("clear")

    confirm = input(f"Are you sure you want to delete '{author.name}'? (y/N): ").strip().lower()
    if confirm == 'y':
        os.system("clear")
        session.delete(author)
        session.commit()
        print("Author deleted.")
    else:
        print("Cancelled.")


def author_by_name(session: Session, name: str):
    authors = session.query(Authors).filter(Authors.name.ilike(f"%{name}%")).all()

    if not authors:
        print("No authors found.")
        return None

    os.system("clear")

    print(f"\nSearch Results for '{name}'\n")

    results = []
    
    for author in authors:
        total_books = session.query(Books).filter_by(author_id=author.author_id).count()

        result = {
            "name": author.name,
            "total_books": total_books
        }
        results.append(result)

        print(f"Author  : {result['name']}")
        print(f"Books : {result['total_books']}\n")

    return results
