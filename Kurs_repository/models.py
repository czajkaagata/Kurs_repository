import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)


    from sqlalchemy import Table, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

# Tabela asocjacyjna (łączy filmy z aktorami)
movie_actors = Table(
    'movie_actors',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True)
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer)
    
    # Relacja do aktorów
    actors = relationship("Actor", secondary=movie_actors, back_populates="movies")

class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    
    # Relacja do filmów
    movies = relationship("Movie", secondary=movie_actors, back_populates="actors")




class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    # NOWA KOLUMNA:
    published_date = Column(DateTime, default=datetime.datetime.utcnow)