#!/usr/bin/python3
"""Defines a FileStorage class."""
import json
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class for handling serialization and
    deserialization of instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects.

        Returns:
            dict: A dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to add.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to a JSON file.
        """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for obj in objs.values():
                cls = obj['__class__']
                if cls in ["Place", "State", "City", "Amenity", "Review"]:
                    self.new(eval(cls)(**obj))
        except FileNotFoundError:
            pass
