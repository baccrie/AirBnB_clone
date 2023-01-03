#!/usr/bin/python3
"""A file Storage Module"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class that handles serialization and de-serialization"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dict objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets an instance to the object attr"""
        key = f"{type(obj).__name__}.{obj.id}"
        value = obj
        FileStorage.__objects[key] = value

    def save(self):
        """Serializez the object attr to file path"""
        file = FileStorage.__objects
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            save_to_file = {k: value.to_dict() for k, value in file.items()}
            json.dump(save_to_file, f)

    def reload(self):
        """Reload from storage engine file to an attr"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for obj_dict in data.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        else:
            return
