#!/usr/bin/python3
"""
Unittest module for testing BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Defines unit tests for BaseModel class."""

    def test_init(self):
        """Test if a new BaseModel is correctly initialized."""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updayed_at, datetime)

    def test_unique_id(self):
        """Test if each instance has a unique id."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_save(self):
        """Test if save() updates the updated_at attribute."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertTrue(instance.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test if to_dict() returns a correct dictionary representation."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(
                instance_dict["created_at"],
                instance.created_at.isoformat()
        )
        self.assertEqual(
                instance_dict["updated_at"],
                instance.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()
