#!/usr/bin/python3
"""The interactive console for Admimistrative use"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """A Console class that inherits from cmd"""
    prompt = '(hbnb) '
    class_names = ['BaseModel']

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """create: Creates a new instance of BaseModel, saves it
        (to the JSON file)and prints the id"""
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            if arg[0] not in self.class_names:
                print("** class doesn't exist **")
            else:
                new = BaseModel()
                new.save()
                print(new.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id."""
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            if arg[0] not in self.class_names:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg) == 2:
            new = FileStorage()
            new.reload()
            all = new.all()
            val = all.keys()
            search = f"{arg[0]}.{arg[1]}"
            if (search not in all.keys()):
                print("** no instance found **")
            for key, value in all.items():
                if (key == search):
                    print(value)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            if arg[0] not in self.class_names:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(arg) == 2:
            new = FileStorage()
            new.reload()
            all = new.all()
            val = all.keys()
            search = f"{arg[0]}.{arg[1]}"
            if (search not in all.keys()):
                print("** no instance found **")
                return
            del all[search]
            new.__objects = all
            new.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name."""
        arg = line.split()
        new = FileStorage()
        new.reload()
        all = new.all()
        if len(arg) == 0:
            for key, value in all.items():
                print(value)
        elif len(arg) == 1:
            if arg[0] not in self.class_names:
                print("** class doesn't exist **")
                return
            for key, value in all.items():
                if type(value).__name__ == arg[0]:
                    print(value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
