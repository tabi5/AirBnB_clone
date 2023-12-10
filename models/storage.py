#!/usr/bin/python3
"""Defines a FileStorage class."""
import json


class Storage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): a name of a file to save objects to.
        __objects (dict): a dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        objects_dict = FileStorage.__objects
        return objects_dict

    def new(self, obj):
        """Set in __objects obj with a key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to a JSON file __file_path."""
        objects_dict = FileStorage.__objects
        objdict = {
            obj: objects_dict[obj].to_dict()
            for obj in objects_dict.keys()
        }
        json_data = json.dumps(objdict)
        with open(FileStorage.__file_path, "w") as f:
            f.write(json_data)

    def reload(self):
        """Deserialize a JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    new_obj_dict ={
                            k: v for k, v in o.items() if k != "__class__"
                    }
                    self.new
                    (
                        eval(cls_name)(**new_obj_dict)
                    )
        except FileNotFoundError:
            return
