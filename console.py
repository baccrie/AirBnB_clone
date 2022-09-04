#!/usr/bin/python3
"""
A module that splips into an interactive session
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class that incorporates a command line interpreter
    """
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        return (True)
    
    def do_EOF(self, line):
        return (True)   
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()