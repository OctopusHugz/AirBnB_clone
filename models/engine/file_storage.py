#!/usr/bin/env python3
"""This module creates a FileStorage class"""
from uuid import uuid4
from datetime import datetime
from os.path import exists
import json


class FileStorage:
    """This is an instance of the FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This function returns the dictionary FileStorage.__objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This function sets in __objects the obj with key <obj class name>.id"""
        key_string = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_string] = obj.to_dict()

    def save(self):
        """This function serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as fp:
            fp.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """This function deserializes the JSON file to __objects, if the JSON file exists"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as fp:
                object_string = fp.read()
            return json.loads(object_string)
