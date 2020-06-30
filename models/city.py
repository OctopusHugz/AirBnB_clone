#!/usr/bin/env python3
"""This module creates an instance of the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is an instance of the City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates the City instance"""
        super().__init__(**kwargs)
