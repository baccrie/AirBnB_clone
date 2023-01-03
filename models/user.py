#!/usr/bin/python3
"""A magical module"""

from models.base_model import BaseModel

class User(BaseModel):
    """A module thah inherits from base Module"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
