#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    """ (Task 9) Defines a relationship between the User and Review classes."""
    reviews = relationship("Review", cascade="all, delete", backref="user")


