#!/usr/bin/env python3
"""This module creates the HBNB interactive console"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel, saves it to the JSON file and print the id\n"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":  # make list with different classes?
            print("** class doesn't exist **")
        else:
            new_model = BaseModel(arg)
            print(new_model.id)
            new_model.save()

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
        elif string_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(string_list) != 2:
            print("** instance id missing **")
        else:
            console_storage = storage.all()
            try:
                instance = BaseModel(console_storage[instance_id])
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
        elif string_list[0] != "BaseModel":
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
        if not arg:
            for obj_id in console_storage:
                print(console_storage[obj_id])
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            for obj_id in console_storage:
                if console_storage[obj_id]["__class__"] == arg:
                    print(console_storage[obj_id])

    def do_update(self, arg):
        """Update command to add or update an instance's attribute based on the class name and id, then save the change into the JSON file\n"""
        l = len(arg.split())
        c = "BaseModel"
        if l < 1:
            print("** class name missing **")
            return
        name = arg.split()[0]
        if name != c:
            print("** class doesn't exist **")
            return
        if l < 2:
            print("** instance id missing **")
            return
        object_id = arg.split()[1]
        if l < 3:
            print("** attribute name missing **")
            return
        key = arg.split()[2]
        if l < 4:
            print("** value missing **")
            return
        value = arg.split()[3]
        s = storage.all()
        b = BaseModel()
        b.update(name, object_id, key, value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
