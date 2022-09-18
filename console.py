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
        """
        a method that ensures nothing is printed when an empty line is executed
        """
        pass

    def do_create(self, attr):
        """
        This method cretaes a new instance of the base
        model or base model descandants
        """
        attr = attr.split()
        if not attr:
            print("** class name missing **")
        elif attr[0] not in self.classes:
            print("** class doesn't exist **")
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
            print("** class doesn't exist **")
        elif (len(attr) == 1):
            print("** instance id missing **")
        elif (attr and attr[1]):
            attr_2 = f"{attr[0]}.{attr[1]}"
            if attr_2 not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.reload()
                obj = storage.all()
                attr_2 = f"{attr[0]}.{attr[1]}"
                for key, value in obj.items():
                    if key == attr_2:
                        print(value)

    def do_destroy(self, attr):
        """
        Deletes an instance from the file storage engine
        """
        attr = attr.split()
        if not attr:
            print("** class name missing **")
        elif attr and attr[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(attr) == 1:
            print("** instance id missing **")
        elif (attr and attr[1]):
            attr_2 = f"{attr[0]}.{attr[1]}"
            if attr_2 not in storage.all().keys():
                print("** no instance found **")
            else:
                key = f"{attr[0]}.{attr[1]}"
                storage.all().pop(key)
                storage.save()

    def do_all(self, attr):
        """
         Prints all string representation of all
         instances based or not on the class name
         """
        attr = attr.split()
        if (not attr):
            obj = [f"{values}" for key, values in storage.all().items()]
        else:
            obj = [f"{values}" for key, values in
                    storage.all().items() if attr[0] == type(values).__name__]
        print(obj)

    def do_update(self, attr):
        """
        tmp
        """
        attr = attr.split()
        if not attr:
            print("** class name missing **")
        elif attr and attr[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(attr) == 1:
            print("** instance id missing **")
        elif (attr and attr[1]):
            attr_2 = f"{attr[0]}.{attr[1]}"
            if attr_2 not in storage.all().keys():
                print("** no instance found **")
        elif (len(attr) == 2):
            print("** attribute name missing **")
        elif (len(attr) == 3):
            print("** value missing **")
        else:
            key = f"{attr[0]}.{attr[1]}"
            obj = storage.all()
            for keys, values in obj.items():
                if keys == key:
                    values[attr[2]] = attr[3]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
