#!/usr/bin/python3

""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
import models
from models.review import Review
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    
    """ A place to stay """
    
    __tablename__ = 'places'
    
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

reviews = relationship("Review", backref="place", cascade="delete")
amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False)

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 nullable=False, primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 nullable=False, primary_key=True))

if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Getter in case of file storage """
            return [review for review in models.storage.all(Review)
                    if review.state_id == self.id]

        @property
        def amenities(self):
            """ Getter in case of file storage """
            return [amenity for amenity in models.storage.all(Amenity)
                    if amenity.id in self.amenity_ids]

        @amenities.getter
        def amenities(self, obj):
            """ Setter in case of file storage"""
            if type(obj) == Amenity():
                self.amenity_ids.append(obj)
