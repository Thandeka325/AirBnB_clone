#!/usr/bin/python3
"""
Models package initializer that creates a unique FileStorage instance.
"""

from models.engine.file_storage import FileStorage


# Create and load storage instance
storage = FileStorage()
storage.reload()
