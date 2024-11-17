#!/usr/bin/python3
"""
FileStorage module that serializes instances to a JSON file and
deserializes JSON file to instance.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Handles long_term storage of all hbnb models in JSON format.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the object in __objects with the key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value.get("__class__")
                    if cls_name and cls_name in globals():
                        cls = globals()[cls_name]
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted or invalid.")
