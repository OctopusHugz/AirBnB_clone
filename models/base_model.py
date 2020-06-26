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
