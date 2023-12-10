#!/usr/bin/python3
"""IT Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for a testing instantiation of the FileStorage class."""

    def test_file_storage_instantiation_no_args(self):
        file_storage = FileStorage()
        self.assertEqual(type(file_storage), FileStorage)

    def test_file_storage_instantiation_with_arg_raises_error(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        file_storage = FileStorage()
        self.assertEqual(str, type(file_storage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        file_storage = FileStorage()
        self.assertEqual(dict, type(file_storage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for the testing methods of the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp_file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)

        all_objects = models.storage.all()

        self.assertIn("BaseModel." + base_model.id, all_objects.keys())
        self.assertIn(base_model, all_objects.values())

        self.assertIn("User." + user.id, all_objects.keys())
        self.assertIn(user, all_objects.values())

        self.assertIn("State." + state.id, all_objects.keys())
        self.assertIn(state, all_objects.values())

        self.assertIn("Place." + place.id, all_objects.keys())
        self.assertIn(place, all_objects.values())

        self.assertIn("City." + city.id, all_objects.keys())
        self.assertIn(city, all_objects.values())

        self.assertIn("Amenity." + amenity.id, all_objects.keys())
        self.assertIn(amenity, all_objects.values())

        self.assertIn("Review." + review.id, all_objects.keys())
        self.assertIn(review, all_objects.values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        base_model_obj = BaseModel()
        user_obj = User()
        state_obj = State()
        place_obj = Place()
        city_obj = City()
        amenity_obj = Amenity()
        review_obj = Review()
        models.storage.new(base_model_obj)
        models.storage.new(user_obj)
        models.storage.new(state_obj)
        models.storage.new(place_obj)
        models.storage.new(city_obj)
        models.storage.new(amenity_obj)
        models.storage.new(review_obj)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model_obj.id, save_text)
            self.assertIn("User." + user_obj.id, save_text)
            self.assertIn("State." + state_obj.id, save_text)
            self.assertIn("Place." + place_obj.id, save_text)
            self.assertIn("City." + city_obj.id, save_text)
            self.assertIn("Amenity." + amenity_obj.id, save_text)
            self.assertIn("Review." + review_obj.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_model_obj = BaseModel()
        user_obj = User()
        state_obj = State()
        place_obj = Place()
        city_obj = City()
        amenity_obj = Amenity()
        review_obj = Review()
        models.storage.new(base_model_obj)
        models.storage.new(user_obj)
        models.storage.new(state_obj)
        models.storage.new(place_obj)
        models.storage.new(city_obj)
        models.storage.new(amenity_obj)
        models.storage.new(review_obj)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model_obj.id, objects)
        self.assertIn("User." + user_obj.id, objects)
        self.assertIn("State." + state_obj.id, objects)
        self.assertIn("Place." + place_obj.id, objects)
        self.assertIn("City." + city_obj.id, objects)
        self.assertIn("Amenity." + amenity_obj.id, objects)
        self.assertIn("Review." + review_obj.id, objects)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
