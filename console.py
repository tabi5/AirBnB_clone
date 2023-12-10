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
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.lower()
        if class_name not in ["base_model", "place", "state",
                              "city", "amenity", "review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
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
        """Print all string representations of all instances"""
        args = arg.split()
        class_name = args[0] if len(args) > 0 else None
        if class_name and class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        instances = []
        if class_name:
            instances = [str(instance) for key, instance in storage.all().items()
                         if key.startswith(class_name)]
        else:
            instances = [str(instance) for instance in storage.all().values()]
        print(instances)

    def do_update(self, arg):
        """Update an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute, value)
        instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
