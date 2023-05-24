#!/usr/bin/python3
"""
    entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


def parser(arg):
    input_list = []
    word = ""
    arg = arg.replace('"', "")
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

class_name = {"BaseModel": BaseModel().__class__.__name__, "User":User.__class__.__name__}

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
            if arg not in class_name.keys():
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
                if vals[0] not in class_name.keys():
                    print("** class doesn't exist **")
                elif len(vals) > 2:
                    pass
                else:
                    print("** instance id missing **")
            else:
                if vals[0] not in class_name.keys():
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
                        del all_objects[inst_name]
                        storage.save()
                    else:
                        print("** no instance found **")
    
    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
            Usage: all
                 : all <class name>
        """
        if not arg:
            all_instances = storage.all()
            print(all_instances)
        else:
            if arg not in class_name.keys():
                print("** class doesn't exist **")
            else:
                all_instances = storage.all()
                for inst in all_instances.keys():
                    keyname = inst.split(".")
                    if arg == keyname[0]:
                        objects = all_instances[inst]
                        print(objects)
    
    def do_update(self, arg):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
            Usage:
                update <class name> <id> <attribute name>
                  "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
        else:
            vals = parser(arg)
            if len(vals) == 4:
                if vals[0] not in class_name.keys():
                    print("** class doesn't exist **")
                else:
                    all_objects = storage.all()
                    inst_name = "{}.{}".format(vals[0], vals[1])
                    if inst_name in all_objects:
                        # instance exists
                        to_update = all_objects[inst_name]
                        to_update.__dict__[vals[2]] = vals[3]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                if len(vals) == 3:
                    if vals[0] not in class_name.keys():
                        print("** class doesn't exist **")
                    else:
                        inst_name = "{}.{}".format(vals[0], vals[1])
                        all_objects = storage.all()
                        if inst_name in all_objects:
                            print("** value missing **")
                        else:
                            print("** no instance found **")
                else:
                    if len(vals) == 2:
                        if vals[0] not in class_name.keys():
                            print("** class doesn't exist **")
                        else:
                            inst_name = "{}.{}".format(vals[0], vals[1])
                            all_objects = storage.all()
                            if inst_name in all_objects:
                                print("** attribute name missing **")
                            else:
                                print("** no instance found **")
                    else:
                        if len(vals) == 1:
                            if vals[0] not in class_name.keys():
                                print("** class doesn't exist **")
                            else:
                                print("** instance id missing **")
                        else:
                            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
