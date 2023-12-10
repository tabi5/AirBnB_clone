#!/usr/bin/python3
"""
Defines the Review class.

This module defines the Review class, which represents a review.

Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who wrote the review.
    text (str): The text content of the review.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
