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

# List of supported classes
classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
}


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

    def precmd(self, line):
        """Interprets and parse commands like `<class name>.command()`."""
        match = re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            cls_name, command, args = match.groups()
            args = args.strip()
            if command == "update" and args.startswith("{"):
                line = f"{command} {cls_name} {args}"
            else:
                args = args.replace(",", " ").strip()
                line = f"{command} {cls_name} {args}"
        return line

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
        args = parse(arg)

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == args[0])
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
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        cls_name = args[0]
        new_instance = eval(cls_name)()
        for attr in args[1:]:
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
        args = parse(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = obj_dict.get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id."""
        args = parse(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict[key]
            storage.save()

    def do_all(self, arg):
        """Show all instances of a class or all instances"""
        args = parse(arg)
        obj_list = []
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if len(args) == 0 or obj.__class__.__name__ == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id."""
        args = parse(arg)
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) == 3:
            try:
                attr_dict = eval(args[2])
                if isinstance(attr_dict, dict):
                    for k, v in attr_dict.items():
                        setattr(obj_dict[key], k, v)
                    storage.save()
                    return
            except (SyntaxError, NameError):
                print("** value missing **")
                return

        if len(args) == 4:
            obj = obj_dict[key]
            attr_name, attr_value = args[2], args[3]
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
