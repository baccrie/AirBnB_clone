#!/usr/bin/python3
import uuid
from datetime import datetime


""""
A module that contains the base class for all other classes
"""

class BaseModel:
    """""
    The base class for all other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """
        A method that prints  the class
        """
        return (f"[{type(self).__name__}] {self.id} {self.__dict__}")
    
    def save(self):
        """
        A method that updates the current date and time of an instance when invoked
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """"
        A method that returns a dict containing all key/value pairs of an instance
        """
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (dict)