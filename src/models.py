import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table #Table lo agregamos porque hay que importarlo, sino da error.
from sqlalchemy.orm import relationship, declarative_base, backref #backref lo agregamos porque hay que importarlo, sino da error.
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()
followers = Table('followers',Base.metadata, #lo de Base.metadata se lo agregamos nosotros para que funcione, no esta en la documentacion.
    Column('user_to_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True)
)
#las dos propiedades que nos da la academia para hacer el ejercicio pasan a estar en la nueva tabla que creamos, y en la vieja
#se agrega la primary key de la clase padre (User) porque asi lo dice la documentacion.
# class Follower(Base):
#     __tablename__ = 'follower'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)  #esto se lo agregamos porque asi dice la documentacion
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followers = relationship('Follower', secondary=followers, lazy='subquery',
        backref=backref('user', lazy=True)) #esto se lo agregamos porque asi dice la documentacion
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_post = Column(String(250),ForeignKey('post.id'))
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_user = Column(String(250),ForeignKey('user.id'))
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    id_user = Column(String(250),ForeignKey('user.id'))
    id_post = Column(String(250),ForeignKey('post.id'))
# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
