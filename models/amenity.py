#!/usr/bin/python3
"""Defines the Amenity class, which inherits from BaseModel."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity for the hbnb.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
