#!/usr/bin/python3
"""Unittest for HBNB console."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage


class TESTHBNBCommand(unittest.TestCase):
    """Tests for the HBNB console."""

    def setUp(self):
        """Prepare test environment."""
        storage.all().clear()

    def test_help(self):
        """Test the `help` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
        self.assertIn("Documented commands", output)

    def test_create(self):
        """Test the `create` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertTrue(user_id in storage.all())

    def test_show(self):
        """Test the `show` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_destroy(self):
        """Test the `destroy` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")
            output = f.getvalue().strip()
        self.assertNotIn(user_id, storage.all())

    def test_all(self):
        """Test the `all` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_update_single(self):
        """Test the `update` command with a single attribute."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} first_name Thandeka")
            output = f.getvalue().strip()
        user = storage.all().get(f"User.{user_id}")
        self.assertEqual(user.first_name, "Thandeka")

    def test_update_dict(self):
        """Test the `update` command with a dictionary."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                f"update User {user_id} {{'age': 29, 'city': 'Cape Town'}}"
            )
            output = f.getvalue().strip()
        user = storage.all().get(f"User.{user_id}")
        self.assertEqual(user.age, 29)
        self.assertEqual(user.city, "Cape Town")

    def test_count(self):
        """Test the `<class>.count()` command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id_1 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id_2 = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
        self.assertEqual(output, "2")

    def test_show_no_instance(self):
        """Test `show` with a missing instance."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_no_instance(self):
        """Test `destroy` with missing instabce."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_no_instance(self):
        """Test `update' with invalid syntax."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_all_no_class(self):
        """Test `all` with no class."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_empty_line(self):
        """Test empty input."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
        self.assertEqual(output, "")


if __name__ == "__main__":
    unittest.main()
