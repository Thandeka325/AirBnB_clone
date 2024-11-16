#!/usr/bin/python3
"""Defines the City class, which inherits from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city for the hbnb.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
