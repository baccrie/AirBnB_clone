#!/usr/bin/python3
"""A class named (BaseModel) that defines all common
attributes/methods for other classes:"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """A Base class"""

    def __init__(self, *args, **kwargs):
        """initialization of object"""
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif (key == 'created_at'):
                    self.created_at = datetime.\
                            strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                elif (key == 'updated_at'):
                    self.updated_at = datetime.\
                            strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints the str repr of an object"""
        ret_value = "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)
        return (ret_value)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
__dict__ of the instance:"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return (dict_copy)
