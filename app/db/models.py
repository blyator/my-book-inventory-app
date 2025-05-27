from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

class Books( Base ):
    __tablename__ = "books"
    
    book_id = Column( Integer, primary_key =True )
    author_id =Column( Integer, ForeignKey("authors.author_id") )
    genre_id =Column( Integer, ForeignKey("genres.genre_id") )
    title =Column( String, nullable = False )

    author = relationship("Authors", back_populates="books")
    genre = relationship("Genres", back_populates="books")



class Authors( Base ):
    __tablename__ = "authors"
    
    author_id = Column( Integer, primary_key =True )
    name =Column( String, nullable = False )

    books = relationship("Books", back_populates="author", cascade="all, delete-orphan")



class Genres( Base ):
    __tablename__ = "genres"
    
    genre_id = Column( Integer, primary_key =True )
    genre =Column( String, nullable = False, unique=True )

    books = relationship("Books", back_populates="genre", cascade="all, delete-orphan")