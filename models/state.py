#!/usr/bin/python3
"""Defines the State class, which inherits from BaseModel."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state for the AirBnB clone (hbnb).

    Attributes:
        name (str): The name of the state.
    """
    name = ""
