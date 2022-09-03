#!/usr/bin/python3
""""
A file storage engine module
"""

import json
import os
import datetime
from models.base_model import BaseModel

class FileStorage:
    """
    A module class that serialises and deserialises
    an instance of classes generated from BaseModel
    """
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """
        Returns a dict containing all instance created
        """
        return (FileStorage.__objects)
    
    def new(self, obj):
        """
        serialises a new instance to the private class attr __objects
        """
        key = type(obj).__name__,".",obj.id
        FileStorage.__objects[key] = obj
        
    #def save(self):
        """
        A method that serialises the object attr to a file
        """
        """new = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new, f)"""
            
    #def reload(self):
        """
        A method that deserializes the JSON file to __object
        """
        
        """if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dict1 = json.load(f)
                new_dict = {key: self.classes()[value["__class__"]](**value)\
                for key, value in dict1.items()}
            FileStorage.__objects = new_dict
                
        else:
            pass"""

    def save(self):
        """save method serializes __objects to JSON file at __filepath"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        json_str = json.dumps(obj_dict)

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """reload method deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
