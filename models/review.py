#!/usr/bin/python3
"""Defines the Review class, which inherits from BaseModel."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review fro the hbnb.

    Attributes:
        place_id (str): The ID of the place being reviewd.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
