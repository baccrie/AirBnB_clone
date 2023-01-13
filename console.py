#!/usr/bin/python3
"""The great console module"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Entry point for the command interpreter"""
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel
            }

    def do_quit(self, line):
        """Exits the console safely"""
        return True

    def do_EOF(self, line):
        """Quits the console"""
        return True

    def emptyline(self):
        """a method that ensures that
        an empty line + ENTER
        shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """a method that Creates a new instance
        of BaseModel or it sub-class, and saves it (to the JSON file)
        """
        if not line:
            print("** class name missing **")
        else:
            if line not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                command = f"{line}()"
                new = eval(command)
                new.save()
                print(new.id)

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            arg = line.split(' ')
            if arg[0] not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                key = f"{arg[0]}.{arg[1]}"
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class
        name and id (save the change into the
        JSON file)"""
        if not line:
            print("** class name missing **")
        else:
            arg = line.split(' ')
            if arg[0] not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                key = f"{arg[0]}.{arg[1]}"
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
