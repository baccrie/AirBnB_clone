#!/usr/bin/python3
"""A file Storage Engine module"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage():
    """A file storage engine"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns all 0bjects"""
        return (self.__objects)

    def new(self, obj):
        """Stores new obj instance to object attr"""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_to_save = {}
        for key, val in self.__objects.items():
            obj_to_save[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as pointer:
            json.dump(obj_to_save, pointer)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        else:
            pass
