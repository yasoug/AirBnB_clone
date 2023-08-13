#!/usr/bin/python3
'''
Defines BaseModel Class
'''
import cmd
import json
import uuid
from datetime import datetime


class BaseModel:
    """
    Represents the BaseModel class for Airbnb clone project
    """

    def __init__(self):
        """
        Initializes new instance of the BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns string representation of BaseModel
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        Updates the attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
