#!/usr/bin/python3
"""
This script sets up the console for the HBnB application.
It imports necessary modules and
model classes required for the functioning of the application.
The models include storage,
BaseModel, User, State, City, Place, Amenity, and Review.
"""
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    valid_classes = ['BaseModel']  # Add more valid classes here

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = BaseModel.load_json()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = BaseModel.load_json()
        if key in objects:
            objects.pop(key)
            BaseModel.save_json(objects)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of all instances based on the class name"""
        args = arg.split()
        objects = BaseModel.load_json()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] in self.valid_classes:
            class_name = args[0]
            filtered_objs = [str(obj) for key, obj in objects.items() if key.split('.')[0] == class_name]
            print(filtered_objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = BaseModel.load_json()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        obj = objects[key]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
                setattr(obj, attr_name, attr_value)
                obj.save()
            except ValueError:
                print("** invalid value **")
        else:
            print("** attribute doesn't exist **")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
