#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class for handling serialization and
    deserialization of instances.

    Attributes:
        __file_path (str): a name of the file to save objects to.
        __objects (dict): the dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to add.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes the objects to a JSON file."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
    
    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    if cls_name == "Place":
                        self.new(Place(**o))
                    elif cls_name == "State":
                        self.new(State(**o))
                    elif cls_name == "City":
                        self.new(City(**o))
                    elif cls_name == "Amenity":
                        self.new(Amenity(**o))
                    elif cls_name == "Review":
                        self.new(Review(**o))
        except FileNotFoundError:
            return
