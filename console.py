#!/usr/bin/python3
"""
    entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


def parser(arg):
    input_list = []
    word = ""
    for letter in range(0, len(arg)):
        if letter == (len(arg) - 1):
            word += arg[letter]
            input_list.append(word)
        else:
            if arg[letter] != " ":
                word += arg[letter]
            else:
                input_list.append(word)
                word = ""
    return input_list

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

    def do_create(self, arg):
        """
            Creates a new instance of base_model
            Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            if arg != BaseModel().__class__.__name__:
                print("** class doesn't exist **")
            else:
                my_Instance = BaseModel()
                my_Instance.save()
                print(my_Instance.id)
    
    def do_show(self, arg):
        """
            Prints string rep of instance
            based on class name
            Usage: show <class_name> <id>
        """
        if not arg:
            print("** class name missing **")
        else:
            vals = parser(arg)
            if len(vals) != 2:
                if vals[0] != BaseModel().__class__.__name__:
                    print("** class doesn't exist **")
                elif len(vals) > 2:
                    pass
                else:
                    print("** instance id missing **")
            else:
                if vals[0] != BaseModel().__class__.__name__:
                    print("** class doesn't exist **")
                else:
                    all_objects = storage.all()
                    inst_name = "{}.{}".format(vals[0], vals[1])
                    if inst_name in all_objects:
                        print(all_objects[inst_name])
                    else:
                        print("** no instance found **")
    
    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            Usage: destroy <class name> <id>
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
