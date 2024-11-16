#!/usr/bin/python3
"""
Console module for the HBNBCommand command interpreter.
"""

import cmd
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


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing HBNB objects."""

    prompt = "(hbnb) "

    def precmd(self, line):
        """Interprets and parse commands like `<class name>.command()`."""
        if '.' in line and '(' in line and ')' in line:
            try:
                cls_name, rest = line.split('.', 1)
                command, args = rest.split('(', 1)
                args = args.rstrip(')')
                if args:
                    args = args.split(',', 1)
                    args = [arg.strip().strip('"').strip("'") for arg in args]
                line = f"{command} {cls_name} {' '.join(args)}"
            except ValueError:
                pass
            return line

    def do_count(self, args):
        """Gets the number of instances of a class."""
        args = args.split()
        if not args or args[0] not in classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for object in storage.all().values()
                    if obj.__class__.name__ == args[0]
        )
        print(count)


    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()    #ensures a new line after EOF
        return True

    def emptyline(self):
        """Overrides the default behaviour to do nothing on an empty line."""
        pass

    def do_create(self, class_name):
        """Creates a new instance of BaseModel, saves it & prints id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Shows instance string representation based on class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Show all instances of a class or all instances"""
        args = args.split()
        obj_list = []
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args[0]:
                obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, args):
        """Updates an instance's attribute(save the change into the JSON file)"""
        args = args.split(" ", 2)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        try:
            attr_dict = eval(args[2])
            if isinstance(attr_dict, dict):
                for attr_name, attr_value in attr_dict.items():
                    try:
                        attr_value = eval(attr_value)
                    except (SyntaxError, NameError):
                        pass
                    setattr(obj, attr_name, attr_value)
                obj.save()
                return
        except (SyntaxError, NameError):
            pass

        attr_parts = args[2].split()
        if len(attr_parts) < 2:
            print("** value missing **")
            return
        attr_name = attr_parts[0]
        attr_value = attr_parts[1]
        try:
            attr_value = eval(attr_value)
        except (SyntaxError, NameError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
