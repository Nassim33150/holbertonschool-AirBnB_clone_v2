#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.engine.db_storage import DBStorage
from models.review import Review
from models.engine.file_storage import FileStorage

class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    """ (Task 9) Defines a relationship between the Place and Review classes."""
    reviews = relationship("Review", cascade="all, delete", backref="place")

    def cities(self):
        """ Retrieve all reviews from storage """
        all_reviews = storage.all(Review)
        place_reviews = [review for review in all_reviews.values()
                        if review.place_id == self.id]

        return place_reviews
