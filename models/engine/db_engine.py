#!/usr/bin/python3
from sqlalchemy import create_engine
from os import environ
from sqlalchemy.orm import sessionmaker, scoped_session

""" Define new class for engine database """
class DBStorage: 
    """ private attributes set to none """
    __engine = None
    __session = None

    def __init__(self):
        """Create the database engine and session"""
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', 'localhost')
        db = environ.get('HBNB_MYSQL_DB')
        
        self.__engine = create_engine('mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))