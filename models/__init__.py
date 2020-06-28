#!/usr/bin/env python3
"""This module creates the models module and creates an FileStorage instance"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
