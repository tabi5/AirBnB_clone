#!/usr/bin/python3
"""
Defines the City class.

This module defines the City class, which represents a city.

Attributes:
    state_id (str): The state ID of the city.
    name (str): The name of the city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The state ID of the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
