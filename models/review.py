#!/usr/bin/python3
"""A module that defines Reviews done by users"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
