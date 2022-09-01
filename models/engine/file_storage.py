#!/usr/bin/python3
""""
A file storage engine module
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    A module class that serialises and deserialises
    an instance of classes generated from BaseModel
    """
    __file_path = "file.json"
    __objects = {}
    
    def classes(self):
        """
        This method is used to import classes
        """
        from models.base_model import BaseModel
        
        classes = {
            "BaseModel": BaseModel
        }    
        
    def all(self):
        """
        Returns a dict containing all instance created
        """
        return (FileStorage.__objects)
    
    def new(self, obj):
        """
        serialises a new instance to the private class attr __objects
        """
        key = type(self).__name__,obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        """
        A method that serialises the object attr to a file
        """
        new = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new, f)
            
    def reload(self):
        """
        A method that deserializes the JSON file to __object
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                dict = json.load(f)
                new_dict = {key: self.classes()[value["__class__"]](**value)\
                for key, value in dict.items()}
                
        else:
            pass