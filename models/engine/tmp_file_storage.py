#!/usr/bin/python3
"""A file Storage Module"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class that handles serialization and de-serialization"""
    __file_path = "file.json"
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
        with open(FileStorage.__file_path, 'w') as f:
            save_to_file = {k: value.to_dict() for k, value in file.items()}
            json.dump(save_to_file, f)

    def reload(self):
        """Reload from storage engine file to an attr"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for obj_dict in data.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        else:
            pass
