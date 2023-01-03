#!/usr/bin/python3
"""The interactive console for Admimistrative use"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A Console class that inherits from cmd"""
    prompt = '(hbnb) '
    intro = 'baccrie copyright © 2022 Doing the hard things sucks'

    def do_EOF(self, arg):
        """Quits the interactive shell safely"""
        exit()

    def do_quit(self, arg):
        """Exits the interactive session"""
        exit()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
