#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.engine.db_storage import DBStorage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.user import User
from models.city import City
from models.place import Place


class Review(BaseModel, Base):
    """ The review class, contains user ID and place ID """
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey(places.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
