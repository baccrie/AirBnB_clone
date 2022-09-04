#!/usr/bin/python3
"""
A module that splips into an interactive session
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A class that incorporates a command line interpreter
    """
    prompt = "(hbnb) "
    classes = ["BaseModel"]
    
    def do_quit(self, line):
        """
        Exits the interactive shell session
        """
        return (True)
    
    def do_EOF(self, line):
        """
        Exits the interactive shell session
        """
        return (True)   
    
    def emptyline(self):
        """"
        a method that ensures nothing is printed when an empty line is executed
        """
        pass    
    
    def do_create(self, attr):
        """
        This method cretaes a new instance of the base model or base model descandants
        """
        attr = attr.split()
        
        if not attr:
            print("** class name missing")
        elif attr[0] not in self.classes:
            print("** class dosen't exist**")
        else:
            new = BaseModel()
            new.save()
            print(new.id)
            
    def do_show(self, attr):
        """
        Prints the dictionary repr of an object with Class name and id
        """
        attr = attr.split()
        if (not attr):
            print("** class name missing **")
        elif (attr and attr[0] not in self.classes):
                print("** class dosent exist **")
        elif (len(attr) == 1):
            print("** instance id missing **")
        else:
            storage.reload()
            obj = storage.all()
            attr_2 = f"{attr[0]}.{attr[1]}"
            for key, value in obj.items():
                if key == attr_2:
                    print(value)
            
            
            
            
            

if __name__ == "__main__":
    HBNBCommand().cmdloop()
