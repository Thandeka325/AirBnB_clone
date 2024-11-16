#!/usr/bin/python3
"""
Unittest module for testing FileStorage class.
"""

import unittest
from models.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """Defines unit tests for FileStorage class."""

    def setup(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        """Test if save() properly writes to file.json."""
        self.storage.save(self.obj)
        with open("file.json", "r") as f:
            data = json.load(f)
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertIn(key, data)

    def test_reload(self):
        """Test if reload() correctly loads objects from file.json."""
        self.storage.save(self.obj)
        self.storage.reload()
        key = f"{self.obj.__class__.name__}.{self.obj.id}"
        self.assertIn(key, self.storage._FileStorage__object)


if __name__ == "__main__":
    unittest.main()
