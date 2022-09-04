#!/usr/bin/python3


import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class that incorporates a command line interpreter
    """
    prompt = "(hbnb) "
    
    def do_quit(self, attr):
        return (True)
    
    def do_EOF(self, attr):
        return (True)     
if __name__ == "__main__":
    HBNBCommand().cmdloop()