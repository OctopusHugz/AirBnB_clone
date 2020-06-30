#!/usr/bin/env python3
"""This module creates the HBNB interactive console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class creates an instance of the HBNB Command interpreter"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]
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

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel, saves it to the JSON file and print the id\n"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_model = BaseModel()
            elif arg == "User":
                new_model = User()
            print(new_model.id)
            storage.new(new_model)
            storage.save()

    def do_show(self, arg):
        """Show command to print the string representation of an instance based on the class name and id\n"""
        string_list = []
        instance_id = ""
        string_list = arg.split(" ")
        if len(string_list) >= 1:
            class_name = string_list[0]
            if len(string_list) == 2:
                obj_id = string_list[1]
                instance_id = class_name + "." + obj_id
        if not arg:
            print("** class name missing **")
        elif string_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(string_list) != 2:
            print("** instance id missing **")
        else:
            console_storage = storage.all()
            try:
                instance = console_storage[instance_id]
                #instance_class = eval(class_name)
                #instance = instance_class(console_storage[instance_id])
                print(instance)
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on the class name and id, then save the change into the JSON file\n"""
        string_list = []
        instance_id = ""
        string_list = arg.split(" ")
        if len(string_list) >= 1:
            class_name = string_list[0]
            if len(string_list) == 2:
                obj_id = string_list[1]
                instance_id = class_name + "." + obj_id
        if not arg:
            print("** class name missing **")
        elif string_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(string_list) != 2:
            print("** instance id missing **")
        else:
            console_storage = storage.all()
            try:
                del (console_storage[instance_id])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """All command to print the string representation of all instances in storage, based on the class name if given. If not, print the string representation of all instances in storage\n"""
        console_storage = storage.all()
        console_s_copy = console_storage.copy()
        instance_list = []
        if not arg:
            for obj_id in console_s_copy:
                #class_name = console_storage[obj_id].__class__.__name__
                #instance_class = eval(class_name)
                #instance = instance_class(console_storage[obj_id])
                instance = (console_storage[obj_id])
                print(instance)
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            for obj_id in console_s_copy:
                if console_storage[obj_id].__class__.__name__ == arg:
                    # Needs to print the instance and not the dict of instance!
                    #instance_class = eval(arg)
                    #instance = instance_class(console_storage[obj_id])
                    #print(instance)
                    print(console_storage[obj_id])

    def do_update(self, arg):
        """Update command to add or update an instance's attribute based on the class name and id, then save the change into the JSON file\n"""
        string_list = []
        instance_id = ""
        string_list = arg.split(" ")
        if len(string_list) >= 1:
            class_name = string_list[0]
            if len(string_list) >= 2:
                obj_id = string_list[1]
                instance_id = class_name + "." + obj_id
                if len(string_list) >= 3:
                    key = string_list[2]
                    if len(string_list) >= 4:
                        value = string_list[3]
        if not arg:
            print("** class name missing **")
        elif string_list[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(string_list) < 2:
            print("** instance id missing **")
        elif len(string_list) < 3:
            print("** attribute name missing **")
        elif len(string_list) < 4:
            print("** value missing **")
        else:
            s = storage.all()
            for obj_id in s:
                if type(s[obj_id]) != dict:
                    s[obj_id] = s[obj_id].to_dict()
            value = value.strip("\"")
            # The attribute value must be casted to the attribute type
            s[instance_id].update({key: value})
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
