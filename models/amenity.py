#!/usr/bin/env python3
"""This module creates an instance of the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This is an instance of the Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """This function creates the Amenity instance"""
        super().__init__(**kwargs)
