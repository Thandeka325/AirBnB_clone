#!/usr/bin/python3
"""Defines the User class, which inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user for the AirBnb clone(hbnb).

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
