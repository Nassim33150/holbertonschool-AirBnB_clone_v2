#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def cities(self):
        """ Retrieve all cities from storage """
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values()
                        if city.state_id == self.id]

        return state_cities
