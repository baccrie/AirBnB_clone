#!/usr/bin/python3
"""The great console module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point for the command interpreter"""
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
