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
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
