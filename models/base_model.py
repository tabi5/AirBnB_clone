#!/usr/bin/python3
"""it Defines the BaseModel class."""
import uuid
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Represents a BaseModel of the HBnB project."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """it Update updated_at with the current datetime."""
        current_time = datetime.today()
        self.updated_at = current_time
        models.storage.save()

    def to_dict(self):
        """Return a dictionary of the BaseModel instance.

        Includes a key/value pair __class__ representing
        the class name of a object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        class_name = self.__class__.__name__
        rdict["__class__"] = class_name
        return rdict

    def __str__(self):
        """Return a print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
