#!/usr/bin/python3
"""FileStorage module"""


import json
from models.base_model import BaseModel
import os


class FileStorage:
    """
    A class that serialises and deserialises
    an instance of classes generated from BaseModel
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """this method returns dictionary of private class attr objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """new method which adds object to __objects dict
        Args:
            obj (object): object to add to dictionary
        """
        key = f"{type(self).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        A method that serialises the object attr to a file
        """
        new = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new, f)

    """def reload(self):
        reload method deserializes the JSON file to __objects
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
        """
        
    def reload(self):
        """
        A method that deserialises file_storage to objects attribute
        """
        obj = {}
        if (os.path.exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as f:
                obj_conv = json.load(f)
                for value in obj_conv.values():
                    cls = value['__class__']
                    self.new(eval('{}({})'.format(cls, '**value')))
        else:
            pass