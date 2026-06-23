from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase

engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

