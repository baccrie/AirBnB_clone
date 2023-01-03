#!/usr/bin/python3
"""
Defines city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseModel and defines city"""
    state_id = ""
    name = ""
