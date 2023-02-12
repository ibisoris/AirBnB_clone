#!/usr/bin/python3
""" Base Model module """


""" Import uuid4 and datetime """

from uuid import uuid4
from datetime import datetime

class BaseModel:

    """ Class whish will act as the base for other classes """

    def __init__(self):

        """ Initializes instance attributes """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):

        """ Returns an official string representation """

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):

        """ Updates the public instance attribute, updated_at """

        self.updated_at = datetime.now()

    def to_dict(self):

        """ Returns a dictionary containing all keys/values of __dict__ """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict