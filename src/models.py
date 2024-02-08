import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
followers = Table('followers', Base.metadata,
    Column('follower_use_from_id', Integer, ForeignKey('follower.use_from_id'), primary_key=True), 
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
) 
#las dos propiedades que nos da la academia para hacer el ejercicio pasan a estar en la nueva tabla que creamos, y en la vieja
#se agrega la primary key de la clase padre (User) porque asi lo dice la documentacion.

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    firstname = Column(String(250), nullable=True)
    lastname = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    posts = relationship('Post', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    follower = relationship('Follower', secondary=followers, lazy='subquery', backref='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = relationship('Comment', backref='post', lazy=True)
    medias = relationship('Media', backref='post', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_ = Column(Integer, nullable=True)
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    use_from_id = Column(Integer, primary_key=True)
    # followers = relationship('User', secondary=followers, backref='follower', lazy=True)
    

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
