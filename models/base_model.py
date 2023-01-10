#!/usr/bin/python3
"""A base module that all other module inherits fron"""


import uuid
from datetime import datetime


class BaseModel:
    """A Base model with three common attr"""

    def __init__(self):
        """an instance method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A method that returns a str repr"""
        ret_str = f"[{type(self).__name__}] ({self.id}) {self.id}"
        return (ret_str)

    def save(self):
        """Saves an instance to a json file"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """converts the dict repr and returns it"""
        dict_conv = self.__dict__.copy()
        dict_conv['__class__'] = f"{type(self).__name__}"
        dict_conv['created_at'] = dict_conv['created_at'].isoformat()
        dict_conv['updated_at'] = dict_conv['updated_at'].isoformat()
        return (dict_conv)
