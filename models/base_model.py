#!/usr/bin/env python3
"""This module creates a Base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is an instance of the BaseModel class"""

    def __init__(self):
        """This function creates an instance of the BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This function returns the string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update with current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel"""
        d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d
