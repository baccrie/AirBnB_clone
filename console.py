#!/usr/bin/python3
"""The great console module"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point for the command interpreter"""
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    methods = ['all', 'show', 'count', 'update', 'destroy']
    classe = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

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

    def do_all(self, line):
        """Prints all string representation of
        all instances based or
        not on the class name"""
        list_of_obj = []
        if not line:
            for key, val in storage.all().items():
                list_of_obj.append(f"{val}")
            print(list_of_obj)
        else:
            if line not in self.classes.keys():
                print("** class doesn't exist **")
            else:
                for key, val in storage.all().items():
                    if type(val).__name__ == line:
                        list_of_obj.append(f"{val}")
                print(list_of_obj)

    def do_update(self, line):
        """This method Updates an instance based
        on the class name and id by adding or
        updating attribute (save the change into
        the JSON file)."""
        if not line:
            print("** class name missing **")
        else:
            arg = line.split(' ')
            if arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(arg) == 1:
                print("** instance id missing **")
            elif len(arg) == 2:
                key = f"{arg[0]}.{arg[1]}"
                if key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            elif len(arg) == 4:
                search = f"{arg[0]}.{arg[1]}"
                if search not in storage.all().keys():
                    print("** no instance found **")
                for k, v in storage.all().items():
                    if search == k:
                        setattr(v, arg[2], (arg[3]))
                        v.save()

    def precmd(self, line):
        """A method that do hard things"""

        if line == '' or not line.endswith(')'):
            return line

        flag = 1

        for x in self.classe:
            for y in self.methods:
                if line.startswith("{}.{}(".format(x, y)):
                    flag = 0
        if flag:
            return line

        tmp = ''
        for x in self.methods:
            tmp = line.replace('(', '.').replace(')', '.').split('.')
            if tmp[0] not in self.classe:
                return ' '.join(tmp)
            while tmp[-1] == '':
                tmp.pop()
            if len(tmp) < 2:
                return line
            if len(tmp) == 2:
                tmp = '{} {}'.format(tmp[1], tmp[0])
            else:
                tmp = '{} {} {}'.format(tmp[1], tmp[0], tmp[2])
            if tmp.startswith(x):
                return tmp

        return ''


if __name__ == '__main__':
    HBNBCommand().cmdloop()
