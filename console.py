#!/usr/bin/env python3
"""This module creates the HBNB interactive console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class creates an instance of the HBNB Command interpreter"""
    prompt = "(hbnb) "
    # Do we need to override do_help(self, arg) or can we just use docstring?

    def do_quit(self, arg):
        """Quit command to exit the console\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the console\n"""
        print()
        exit()

    def emptyline(self):
        """Empty line method that does nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
