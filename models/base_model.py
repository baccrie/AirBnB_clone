#!/usr/biin/python3


from uuid import uuid


""""
A module that contains the base class for all other classes
""""

class BaseModel:
    """""
    The base class for all other classes
    """
    def __init__(self):
        self.id = uuid.uuid4()
        