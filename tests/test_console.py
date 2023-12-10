#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for the testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        cmd_instance = HBNBCommand()
        cmd_instance.prompt = "(new_prompt) "
        self.assertEqual("(new_prompt) ", cmd_instance.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for the testing help messages of
    the HBNB command interpreter.
    """

    def test_help_quit(self):
        h = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = ("Usage: create <class>\n "
             "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = ("Usage: show <class> <id> or <class>.show(<id>)\n "
             "Display the string representation of a class instance of"
             " a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = ("Usage: destroy <class> <id> or <class>.destroy(<id>)\n "
             "Delete a class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = ("Usage: all or all <class> or <class>.all()\n "
             "Display string representations of all instances of a given class"
             ".\n If no class is specified, displays all instantiated "
             "objects.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = ("Usage: count <class> or <class>.count()\n "
             "Retrieve the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = ("Usage: update <class> <id> <attribute_name> <attribute_value> or"
             "\n <class>.update(<id>, <attribute_name>, <attribute_value"
             ">) or\n <class>.update(<id>, <dictionary>)\n "
             "Update a class instance of a given id by adding or updating\n "
             " a given attribute key/value pair or dictionary.")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF all count create destroy help quit show update")
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertFalse(cmd_instance.onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertTrue(cmd_instance.onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            cmd_instance = HBNBCommand()
            cmd_instance.prompt = "(new_prompt) "
            self.assertTrue(cmd_instance.onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        expected_output = "** class name missing **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            command.onecmd("create")
            self.assertFalse(command.do_create(""))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_class(self):
        expected_output = "** class doesn't exist **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        expected_output = "*** Unknown syntax: MyModel.create()"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("MyModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        expected_output = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("BaseModel.create()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_create_object(self):
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for testing show from the HBNB command interpreter"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        expected_output = "** class name missing **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd(".show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_invalid_class(self):
        expected_output = "** class doesn't exist **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("MyModel.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        expected_output = "** instance id missing **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show BaseModel"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show User"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show State"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show City"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Amenity"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Place"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Review"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_id_dot_notation(self):
        expected_output = "** instance id missing **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("BaseModel.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("User.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("State.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("City.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Amenity.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Place.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Review.show()"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_no_instance_found_space_notation(self):
        expected_output = "** no instance found **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show BaseModel 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show User 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show State 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show City 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Amenity 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Place 1"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("show Review 1"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self):
        expected_output = "** no instance found **"
        command = HBNBCommand()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("BaseModel.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("User.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("State.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("City.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Amenity.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Place.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(command.onecmd("Review.show(1)"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_objects_space_notation(self):
        def assert_show_output(model_name, test_id):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model_name}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{model_name}.{testID}"]
                command = f"show {model_name} {testID}"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())

        assert_show_output("BaseModel", test_id)
        assert_show_output("User", test_id)
        assert_show_output("State", test_id)
        assert_show_output("Place", test_id)
        assert_show_output("City", test_id)
        assert_show_output("Amenity", test_id)
        assert_show_output("Review", test_id)

    def test_show_objects_space_notation(self):
        def assert_show_output(model_name, test_id):
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model_name}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{model_name}.{testID}"]
                command = f"{model_name}.show({testID})"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(obj.__str__(), output.getvalue().strip())

        assert_show_output("BaseModel", test_id)
        assert_show_output("User", test_id)
        assert_show_output("State", test_id)
        assert_show_output("Place", test_id)
        assert_show_output("City", test_id)
        assert_show_output("Amenity", test_id)
        assert_show_output("Review", test_id)


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for testing destroy from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        storage.reload()

    def test_destroy_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation_new(self):
        correct = "** instance id missing **"
        models = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {model}"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notation_(self):
        correct = "** instance id missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{model}.destroy()"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{model}.{testID}"]
                command = f"destroy {model} {testID}"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{model}.{testID}"]
                command = f"show {model} {testID}"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                testID = output.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as output:
                obj = storage.all()[f"{model}.{testID}"]
                command = f"{model}.destroy({testID})"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, storage.all())


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        invalid_class = "MyModel"
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"all {invalid_class}"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"{invalid_class}.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for model in models:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            output_value = output.getvalue().strip()
            for model in models:
                self.assertIn(model, output_value)

    def test_all_objects_dot_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for model in models:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".all()"))
            output_value = output.getvalue().strip()
            for model in models:
                self.assertIn(model, output_value)

    def test_all_single_object_space_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for model in models:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"all {model}"))
                self.assertIn(model, output.getvalue().strip())
                for other_model in models:
                    if other_model != model:
                        self.assertNotIn(other_model,
                                         output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        models = ["BaseModel", "User", "State", "Place",
                  "City", "Amenity", "Review"]
        with patch("sys.stdout", new=StringIO()) as output:
            for model in models:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{model}.all()"))
                self.assertIn(model, output.getvalue().strip())
                for other_model in models:
                    if other_model != model:
                        self.assertNotIn(other_model,
                                         output.getvalue().strip())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for testing update from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self):
        correct = "** class name missing **"
        commands = ["update", ".update()"]
        for command in commands:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self):
        correct = "** class doesn't exist **"
        commands = ["update MyModel", "MyModel.update()"]
        for command in commands:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        correct = "** instance id missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {model}"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{model}.update()"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_space_notation(self):
        correct = "** no instance found **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {model} 1"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"{model}.update(1)"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_space_notation(self):
        correct = "** attribute name missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                testId = output.getvalue().strip()
                testCmd = f"update {model} {testId}"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        correct = "** attribute name missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]
        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                testId = output.getvalue().strip()
                testCmd = f"{model}.update({testId})"
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_space_notation(self):
        correct = "** value missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                testId = output.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as output:
                testCmd = f"update {model} {testId} attr_name"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_value_dot_notation(self):
        correct = "** value missing **"
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                testId = output.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as output:
                stCmd = f"{model}.update({{ {testId}: 'attr_name' }})"
                self.assertFalse(HBNBCommand().onecmd(testCmd))
                self.assertEqual(correct, output.getvalue().strip())

    def test_update_valid_string_attr_space_notation(self):
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                testId = output.getvalue().strip()

            testCmd = f"update {model} {testId} attr_name 'attr_value'"
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()[f"{model}.{testId}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_string_attr_dot_notation(self):
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                tId = output.getvalue().strip()

            testCmd = "{}.update({}, 'attr_name', 'attr_value')".format(
                    model, tId
            )
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["{}.{}".format(model, tId)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_int_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} max_guest 98".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_int_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, max_guest, 98)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_float_attr_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} latitude 7.2".format(testId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_float_attr_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            tId = output.getvalue().strip()
        testCmd = "Place.update({}, latitude, 7.2)".format(tId)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["Place.{}".format(tId)].__dict__
        self.assertEqual(7.2, test_dict["latitude"])

    def test_update_valid_dictionary_space_notation(self):
        models = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                testId = output.getvalue().strip()

            testCmd = f"update {model} {testId} "
            testCmd += "{'attr_name': 'attr_value'}"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()[f"{model}.{testId}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_dot_notation(self):
        models = ["BaseModel", "User", "State", "City",
                  "Place", "Amenity", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd(f"create {model}")
                testId = output.getvalue().strip()

            testCmd = f"{model}.update({testId}, "
            testCmd += "{'attr_name': 'attr_value'})"
            HBNBCommand().onecmd(testCmd)
            test_dict = storage.all()[f"{model}.{testId}"].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])

    def test_update_valid_dictionary_with_int_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_int_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'max_guest': 98})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(98, test_dict["max_guest"])

    def test_update_valid_dictionary_with_float_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "update Place {} ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])

    def test_update_valid_dictionary_with_float_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            testId = output.getvalue().strip()
        testCmd = "Place.update({}, ".format(testId)
        testCmd += "{'latitude': 9.8})"
        HBNBCommand().onecmd(testCmd)
        test_dict = storage.all()["Place.{}".format(testId)].__dict__
        self.assertEqual(9.8, test_dict["latitude"])


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for testing count method
    of HBNB comand interpreter.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count MyModel"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        models = ["BaseModel", "User", "State", "Place", "City",
                  "Amenity", "Review"]

        for model in models:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))

            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"count {model}"))
                self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
