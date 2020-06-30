#!/usr/bin/env python3
"""This module creates an instance of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is an instance of the Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """This function creates the Review instance"""
        super().__init__(**kwargs)
