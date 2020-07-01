#!/usr/bin/env python3
"""This module creates the HBNB interactive console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """This class creates an instance of the HBNB Command interpreter"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place",
                  "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the console\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the console\n"""
        print()
        return True

    def emptyline(self):
        """Empty line method that does nothing"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance, save it to the
JSON file and print the id\n"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            if arg == "BaseModel":
                new_model = BaseModel()
            elif arg == "User":
                new_model = User()
            elif arg == "Place":
                new_model = Place()
            elif arg == "State":
                new_model = State()
            elif arg == "City":
                new_model = City()
            elif arg == "Amenity":
                new_model = Amenity()
            elif arg == "Review":
                new_model = Review()
            print(new_model.id)
            new_model.save()

    def do_show(self, arg):
        """Show command to print the string representation of an instance
based on the class name and id\n"""
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
                print(console_storage[instance_id])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on the class name
and id, then save the change into the JSON file\n"""
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
        """All command to print the string representation of all instances in
storage, based on the class name if given. If not, print the
string representation of all instances in storage\n"""
        console_storage = storage.all()
        instance_list = []
        if not arg:
            for obj_id in console_storage:
                instance_list.append(str(console_storage[obj_id]))
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        else:
            for obj_id in console_storage:
                if console_storage[obj_id].__class__.__name__ == arg:
                    instance_list.append(str(console_storage[obj_id]))
        print(instance_list)

    def do_update(self, arg):
        """Update command to add or update an instance's attribute based on
the class name and id, then save the change into the JSON file\n"""
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
            try:
                s[instance_id].update({key: value})
            except:
                print("** no instance found **")
                return
            s[instance_id].update(
                {"updated_at": str(datetime.now().isoformat())})
            storage.save()

    def precmd(self, line):
        """Parses the command entered to see if class_name.command syntax
was used"""
        storage_copy = storage.all()
        count = 0
        all_check = line[-5:-2]
        count_check = line[-7:-2]
        show_check = line[-44:-40]
        cmd_string = ""
        if all_check == "all":
            class_name = line[:-6]
            cmd_string = "all " + class_name
            return cmd_string
        elif count_check == "count":
            class_name = line[:-8]
            for objs in storage_copy:
                if storage_copy[objs].__class__.__name__ == class_name:
                    count += 1
            print(count)
            return ""
        elif show_check == "show":
            instance_id = line[-38:-2]
            class_name = line[:-45]
            cmd_string = "show " + class_name + " " + instance_id
            return cmd_string
        else:
            return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
