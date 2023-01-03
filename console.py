#!/usr/bin/python3
"""The interactive console for Admimistrative use"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A Console class that inherits from cmd"""
    prompt = '(hbnb) '
    intro = 'baccrie copyright © 2022 Doing the hard things sucks'

    def do_EOF(self, line):
        """Quits the interactive shell safely"""
        return True

    def do_quit(self, line):
        """Exits the interactive session"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
