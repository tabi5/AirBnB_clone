#!/usr/bin/python3
"""
Defines the State class.

This module defines the State class, which represents a state.

Attributes:
    name (str): The name of the state.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
