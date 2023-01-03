#!/usr/bin/python3
"""The interactive console for Admimistrative use"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A Console class that inherits from cmd"""
    prompt = '(hbnb) '
    intro = 'baccrie copyright © 2022 Doing the hard things sucks'

    def do_EOF(self, line):
    """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
