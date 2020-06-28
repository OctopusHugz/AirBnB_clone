#!/usr/bin/env python3
"""This module creates a BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """This is an instance of the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """This function creates an instance of the BaseModel class, *args is ignored"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, date_format)
                elif x != "__class__":
                    self.__dict__[x] = y
        # if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
        elif not (kwargs):
            storage.new(self)

    def __str__(self):
        """This function returns the string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the instance's updated_at attribute with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the BaseModel instance"""
        # Do we need to create the dict entirely from the keys in self.__dict__.keys() ?
        # import copy copy.deepcopy(self.__dict__) might be another option ?
        d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d
