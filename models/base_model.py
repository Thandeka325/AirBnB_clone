#!/usr/bin/python3
"""
This module defines the BaseModel class, for all the hbnb models.
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the base model for hbnb project classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance or re-creates one from a dict.

        Args:
                *args (any): Unused positional arguments.
                **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            tform = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    setattr(self, key, datetime.strptime(value, tform))
                elif key is not "__class__":
                    setattr(self, key, value)

        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the instance's updated_at attribute and saves to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__clas__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
