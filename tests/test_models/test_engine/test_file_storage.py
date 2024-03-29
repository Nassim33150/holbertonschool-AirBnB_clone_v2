#!/usr/bin/python3
"""Test unittest for class FileStorage"""
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test fixtures"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test fixtures"""
        self.storage = None

    def test_all(self):
        """Test the all() method
        Add some objects to the storage"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        """Retrieve all objects from the storage"""
        all_objects = self.storage.all()

        """Check if the objects are retrieved correctly"""
        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

    def test_new(self):
        """Test the new() method
        Create a new object"""
        obj = BaseModel()

        """Add the object to the storage"""
        self.storage.new(obj)

        """Check if the object is added correctly"""
        self.assertIn(obj, self.storage.all().values())

    def test_save(self):
        """Test the save() method
        Add some objects to the storage"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)

        """Save the objects to the file"""
        self.storage.save()

        """Check if the file is created and contains the serialized objects"""
        with open(self.storage._FileStorage__file_path, 'r') as file:
            loaded_objects = json.load(file)
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", loaded_objects)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", loaded_objects)

    def test_reload(self):
        """Test the reload() method"""
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
# ... existing code ...

class TestFileStorage(unittest.TestCase):
    # ... existing code ...

    def test_all_with_class_filter(self):
        """Test the all() method with class filter
        Add objects of different classes to the storage"""
        obj1 = BaseModel()
        obj2 = User()
        obj3 = Place()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()

        """Retrieve objects of type BaseModel from the storage"""
        base_models = self.storage.all(BaseModel)

        """Check if only objects of type BaseModel are retrieved"""
        self.assertIn(obj1, base_models.values())
        self.assertNotIn(obj2, base_models.values())
        self.assertNotIn(obj3, base_models.values())

    def test_new_duplicate_object(self):
        """Test the new() method with duplicate object
        Add the same object twice to the storage"""
        obj = BaseModel()

        """Add the object to the storage twice"""
        self.storage.new(obj)
        self.storage.new(obj)

        """Check if the object is added only once"""
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_empty_storage(self):
        """Test the save() method with empty storage
        Save an empty storage to the file"""
        self.storage.save()

        """Check if the file is created and is empty"""
        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_contents = file.read()
        self.assertEqual(file_contents, '{}')

    def test_reload_nonexistent_file(self):
        """Test the reload() method with nonexistent file
        Try to reload the storage from a nonexistent file"""
        self.storage._FileStorage__file_path = 'nonexistent_file.json'
        self.storage.reload()

        """Check if the storage remains empty"""
        self.assertEqual(len(self.storage.all()), 0)

    def test_delete(self):
        """Test the delete() method
        Add an object to the storage and delete it"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        """Delete the object from the storage"""
        self.storage.delete(obj)

        """Check if the object is deleted from the storage"""
        self.assertNotIn(obj, self.storage.all().values())

# ... existing code ...

if __name__ == '__main__':
    unittest.main()
