#!/usr/bin/env python3
"""This module creates an instance of the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is an instance of the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """This function creates an instance of the User class"""
        super().__init__(**kwargs)
