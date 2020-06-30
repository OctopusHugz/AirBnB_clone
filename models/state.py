#!/usr/bin/env python3
"""This module creates an instance of the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This is an instance of the State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates the State instance"""
        super().__init__(**kwargs)
