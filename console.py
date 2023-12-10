#!/usr/bin/python3
"""
This script sets up the console for the HBnB application.
It imports necessary modules and
model classes required for the functioning of the application.
The models include storage,
BaseModel, User, State, City, Place, Amenity, and Review.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """The Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Create a new instance of a BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != "BaseModel" and line != "User":
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                new_obj = BaseModel()
            else:
                new_obj = User()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Show an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City",
                              "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def do_destroy(self, arg):
        """Destroy an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State",
                              "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Retrieve all instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel", "Place", "State", "City",
                       "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        instances = []
        for instance in storage.all().values():
            if instance.__class__.__name__ == arg:
                instances.append(instance.__str__())
        print(instances)

    def do_count(self, arg):
        """IT Retrieve the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in ["BaseModel", "Place", "State", "City",
                       "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        count = 0
        for instance in storage.all().values():
            if instance.__class__.__name__ == arg:
                count += 1
        print(count)

    def do_update(self, line):
        """Update an instance"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] != "BaseModel" and args[0] != "User":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            objects = storage.all()
            if key in objects:
                obj = objects[key]
                attr_name = args[2]
                value = args[3]
                setattr(obj, attr_name, value)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
