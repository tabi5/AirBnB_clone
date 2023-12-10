#!/usr/bin/python3
"""the __init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


def initialize_storage():
    storage = FileStorage()
    storage.reload()

    initialize_storage()
