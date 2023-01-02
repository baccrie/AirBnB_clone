#!/usr/bin/python3
"""A class named (BaseModel) that defines all common attributes/methods for other classes:"""

import uuid
from datetime import datetime

class BaseModel:
    """A Base class"""

    def __init__(self):
        """initialization of object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the str repr of an object"""
        ret_value = f"{[type(self).__name__]} {(self.id)} {self.__dict__}"
        return (ret_value)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return (dict_copy)
