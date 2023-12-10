#!/usr/bin/python3
"""
Defines the Amenity class.

This module defines the Amenity class,
which represents an amenity.

Attributes:
    name (str): The name of the amenity.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
