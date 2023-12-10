#!/usr/bin/python3
"""
This script sets up the console for the HBnB application.
It imports necessary modules and
model classes required for the functioning of the application.
The models include storage,
BaseModel, User, State, City, Place, Amenity, and Review.
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    # Define the patterns for curly braces and square brackets
    curly_braces_pattern = r"\{(.*?)\}"
    brackets_pattern = r"\[(.*?)\]"

    # Find all substrings within curly braces or square brackets
    curly_braces_substrings = re.findall(curly_braces_pattern, arg)
    brackets_substrings = re.findall(brackets_pattern, arg)

    # Remove the substrings within curly braces or
    # square brackets from the input string
    for substring in curly_braces_substrings + brackets_substrings:
        arg = arg.replace(substring, '')

    # Split the input string into a list of substrings
    substrings = arg.split(',')

    # Remove any empty strings from the list
    substrings = [substring for substring in substrings if substring]

    return substrings


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving the empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }

        # Split the input string into a list of substrings
        argl = arg.split('.')

        # Check if the first substring is a key in argdict
        if argl[0] in argdict.keys():
            # If it is, call the corresponding function with
            # the remaining substrings as arguments
            call = "{} {}".format(argl[0], '.'.join(argl[1:]))
            return argdict[argl[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """it Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """the EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        # Remove any leading or trailing whitespace from the input string
        class_name = arg.strip()

        # Check if the class name is missing
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            # Create a new instance of the class and print its id
            new_instance = eval(class_name)()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Usage: it show <class> <id> or <class>.show(<id>)
        Display a string representation of a class instance of a given id.
        """
        # Split the input string into a list of substrings
        argl = arg.split(' ')

        # Check if the class name is missing
        if len(argl) < 1 or not argl[0]:
            print("** class name missing **")
            return False

        # Check if the class doesn't exist
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Check if the instance id is missing
        if len(argl) < 2 or not argl[1]:
            print("** instance id missing **")
            return False

        # Create the key for the object dictionary
        obj_key = "{}.{}".format(argl[0], argl[1])

        # Get the object dictionary
        objdict = storage.all()

        # Check if the instance is found
        if obj_key not in objdict:
            print("** no instance found **")
            return False

        # Print the string representation of the instance
        print(objdict[obj_key])
        return True

    def do_destroy(self, arg):
        """Usage: it destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        # Split the input string into a list of substrings
        argl = arg.split(' ')

        # Check if the class name is missing
        if len(argl) < 1 or not argl[0]:
            print("** class name missing **")
            return False

        # Check if the class doesn't exist
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Check if the instance id is missing
        if len(argl) < 2 or not argl[1]:
            print("** instance id missing **")
            return False

        # Create the key for the object dictionary
        obj_key = "{}.{}".format(argl[0], argl[1])

        # Get the object dictionary
        objdict = storage.all()

        # Check if the instance is found
        if obj_key not in objdict:
            print("** no instance found **")
            return False

        # Delete the instance from the object dictionary
        del objdict[obj_key]
        storage.save()
        return True

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display the string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        # Split the input string into a list of substrings
        argl = arg.split(' ')

        # Check if the class name is missing
        if len(argl) < 1 or not argl[0]:
            # If no class is specified, display all instantiated objects
            for obj in storage.all().values():
                print(obj.__str__())
            return True

        # Check if the class doesn't exist
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Create a list to store the string representations
        # of all instances of the class
        objl = [obj.__str__() for obj in storage.all().values()
                if obj.__class__.__name__ == argl[0]]

        # Print the list
        print(objl)
        return True

    def do_count(self, arg):
        """Usage: it count <class> or <class>.count()
        Retrieve a number of instances of a given class."""
        # Split the input string into a list of substrings
        argl = arg.split(' ')

        # Check if the class name is missing
        if len(argl) < 1 or not argl[0]:
            print("** class name missing **")
            return False

        # Check if the class doesn't exist
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Count the number of instances of the class
        count = sum(1 for obj in storage.all().values()
                    if obj.__class__.__name__ == argl[0])

        # Print the count
        print(count)
        return True

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
