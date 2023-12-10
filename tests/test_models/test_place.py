#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().identifier))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated))

    def test_city_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.cityIdentifier))
        self.assertIn("cityIdentifier", dir(pl))
        self.assertNotIn("cityIdentifier", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.userIdentifier))
        self.assertIn("userIdentifier", dir(pl))
        self.assertNotIn("userIdentifier", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.placeName))
        self.assertIn("placeName", dir(pl))
        self.assertNotIn("placeName", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(str, type(Place.placeDescription))
        self.assertIn("placeDescription", dir(pl))
        self.assertNotIn("placeDescription", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.roomCount))
        self.assertIn("roomCount", dir(pl))
        self.assertNotIn("roomCount", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.bathroomCount))
        self.assertIn("bathroomCount", dir(pl))
        self.assertNotIn("bathroomCount", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.maxGuests))
        self.assertIn("maxGuests", dir(pl))
        self.assertNotIn("maxGuests", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(int, type(Place.nightlyPrice))
        self.assertIn("nightlyPrice", dir(pl))
        self.assertNotIn("nightlyPrice", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.placeLatitude))
        self.assertIn("placeLatitude", dir(pl))
        self.assertNotIn("placeLatitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(float, type(Place.placeLongitude))
        self.assertIn("placeLongitude", dir(pl))
        self.assertNotIn("placeLongitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        pl = Place()
        self.assertEqual(list, type(Place.amenityIdentifiers))
        self.assertIn("amenityIdentifiers", dir(pl))
        self.assertNotIn("amenityIdentifiers", pl.__dict__)

    def test_two_places_unique_ids(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.identifier, pl2.identifier)

    def test_two_places_different_created_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created, pl2.created)

    def test_two_places_different_updated_at(self):
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated, pl2.updated)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.identifier = "123456"
        pl.created = pl.updated = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'identifier': '123456'", plstr)
        self.assertIn("'created': " + dt_repr, plstr)
        self.assertIn("'updated': " + dt_repr, plstr)

    def test_args_unused(self):
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(identifier="345", created=dt_iso, updated=dt_iso)
        self.assertEqual(pl.identifier, "345")
        self.assertEqual(pl.created, dt)
        self.assertEqual(pl.updated, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(identifier=None, created=None, updated=None)


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing the save method of the Place class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated
        pl.save()
        self.assertLess(first_updated_at, pl.updated)

    def test_two_saves(self):
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated
        pl.save()
        second_updated_at = pl.updated
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated)

    def test_save_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        pl = Place()
        pl.save()
        pl_id = "Place." + pl.identifier
        with open("file.json", "r") as f:
            self.assertIn(pl_id, f.read())


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertIsInstance(Place().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertIn("id", pl_dict)
        self.assertIn("created_at", pl_dict)
        self.assertIn("updated_at", pl_dict)
        self.assertIn("__class__", pl_dict)

    def test_to_dict_contains_added_attributes(self):
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        pl_dict = pl.to_dict()
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertIsInstance(pl_dict["id"], str)
        self.assertIsInstance(pl_dict["created_at"], str)
        self.assertIsInstance(pl_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        expected_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


if __name__ == "__main__":
    unittest.main()
