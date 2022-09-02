#!/usr/bin/python3
import uuid
from datetime import datetime
import models

""""
A module that contains the base class for all other classes
"""

class BaseModel:
    """
    The base class for all other classes
    """
    
    def __init__(self, *args, **kwargs):
        if (kwargs) and (kwargs != ""):
            for key in kwargs:
                if (key == "__class__"):
                    pass
                else:
                    if (key == "cretaed_at" or key == "updated_at"):
                        self.__dict__[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
    def __str__(self):
        """
        A method that prints  the class
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """
        A method that updates the current date and time of an instance when invoked
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """"
        A method that returns a dict containing all key/value pairs of an instance
        """
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return (dict)
