from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship # type: ignore
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
    
    
    

class Authors( Base ):
    __tablename__ = "authors"
    
    author_id = Column( Integer, primary_key =True )
    name =Column( String, nullable = False )



class Genres( Base ):
    __tablename__ = "genres"
    
    genre_id = Column( Integer, primary_key =True )
    genre =Column( String, nullable = False )