#!/usr/bin/python3
"""
Console module for the HBNBCommand command interpreter.
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    """Parse arguments with proper handling for nested structures."""
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_brackets:
        start = arg[:curly_brackets.start()]
        dict_part = arg[curly_brackets.start():curly_brackets.end()]
        return split(start) + [dict_part]
    elif brackets:
        start = arg[:brackets.start()]
        list_part = arg[brackets.start():brackets.end()]
        return split(start) + [list_part]
    else:
        return split(arg)


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing HBNB objects."""

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "Place",
            "City",
            "Amenity",
            "Review"
     }

    def default(self, arg):
        """Interprets and parse commands."""
        arg_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "count": self.do_count,
                "destroy": self.do_destroy,
                "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def help_create(self):
        """Displays help for create command"""
        print("Usage: create <class name> [key=value ...]")
        print("Creates a new instance of a class\
                with optional attributes.")

    def help_update(self):
        """Displays help for update command."""
        print("Usage: update <class name> <id> <attribute name> <attributes.")
        print("Or:     <class name>.update(<id>, <attribute name>,\
                <attribute value>)")
        print("Or:     <class name>.update(<id>, <dictionary>)")
        print("Updates attributes or adds new ones to an instance.")

    def do_count(self, arg):
        """Gets the number of instances of a class."""
        argl = parse(arg)

        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == argl[0])
        print(count)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Overrides the default behaviour to do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it & prints id."""
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        cls_name = argl[0]
        new_instance = eval(cls_name)()
        for attr in argl[1:]:
            if "=" in attr:
                key, value = attr.split("=", 1)
                try:
                    if '"' in value or "'" in value:
                        value = value.strip('"').strip("'").replace('_', ' ')
                    elif '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                    setattr(new_instance, key, value)
                except ValueError:
                    pass
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Shows instance string representation based on class name and id."""
        argl = parse(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(argl) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(argl[0], argl[1])
        obj = obj_dict.get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id."""
        argl = parse(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(argl) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(argl[0], argl[1])
        if key not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[key]
            storage.save()

    def do_all(self, arg):
        """Show all instances of a class or all instances"""
        argl = parse(arg)
        obj_list = []
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(argl) == 0 or obj.__class__.__name__ == argl[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        argl = parse(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(argl) < 2:
            print("** instance id missing **")
            return
        key = f"{argl[0]}.{argl[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(argl) == 3:
            try:
                attr_dict = eval(argl[2])
                if isinstance(attr_dict, dict):
                    for k, v in attr_dict.items():
                        setattr(obj_dict[key], k, v)
                    storage.save()
                    return
            except (SyntaxError, NameError):
                print("** value missing **")
                return

        if len(argl) == 4:
            obj = obj_dict[key]
            attr_name, attr_value = argl[2], argl[3]
            try:
                attr_value = eval(attr_value)
            except (SyntaxError, NameError):
                pass
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
