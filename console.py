#!/usr/bin/python3
"""
    entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Defines the Command Interpreter
        attributes: (str) Command Prompt
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
            Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
            Exits the program
            prints a new line before it exits
        """
        print()
        return True

    def emptyline(self):
        """
            called when an empty line is passed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
