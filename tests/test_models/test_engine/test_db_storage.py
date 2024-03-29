import unittest
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.db = DBStorage()

    def tearDown(self):
        """Clean up the test environment"""
        self.db.delete()

    def test_all(self):
        """Test the all method"""
        # Create some objects
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        # Add objects to the database
        self.db.new(user)
        self.db.new(state)
        self.db.new(city)
        self.db.new(amenity)
        self.db.new(place)
        self.db.new(review)
        self.db.save()

        # Retrieve all objects from the database
        objects = self.db.all()

        # Check if all objects are retrieved
        self.assertIn(user, objects.values())
        self.assertIn(state, objects.values())
        self.assertIn(city, objects.values())
        self.assertIn(amenity, objects.values())
        self.assertIn(place, objects.values())
        self.assertIn(review, objects.values())

    def test_new(self):
        """Test the new method"""
        # Create an object
        user = User()

        # Add the object to the database
        self.db.new(user)
        self.db.save()

        # Retrieve the object from the database
        objects = self.db.all()

        # Check if the object is retrieved
        self.assertIn(user, objects.values())

    def test_save(self):
        """Test the save method"""
        # Create an object
        user = User()

        # Add the object to the database
        self.db.new(user)

        # Save the changes
        self.db.save()

        # Retrieve the object from the database
        objects = self.db.all()

        # Check if the object is retrieved
        self.assertIn(user, objects.values())

    def test_delete(self):
        """Test the delete method"""
        # Create an object
        user = User()

        # Add the object to the database
        self.db.new(user)
        self.db.save()

        # Delete the object from the database
        self.db.delete(user)
        self.db.save()

        # Retrieve the object from the database
        objects = self.db.all()

        # Check if the object is deleted
        self.assertNotIn(user, objects.values())


if __name__ == '__main__':
    unittest.main()
# ...

class TestDBStorage(unittest.TestCase):
    # ...

    def test_all_with_class(self):
        """Test the all method with a specific class"""
        # Create some objects
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        # Add objects to the database
        self.db.new(user)
        self.db.new(state)
        self.db.new(city)
        self.db.new(amenity)
        self.db.new(place)
        self.db.new(review)
        self.db.save()

        # Retrieve objects of a specific class from the database
        objects = self.db.all(cls='User')

        # Check if objects of the specified class are retrieved
        self.assertIn(user, objects.values())
        self.assertNotIn(state, objects.values())
        self.assertNotIn(city, objects.values())
        self.assertNotIn(amenity, objects.values())
        self.assertNotIn(place, objects.values())
        self.assertNotIn(review, objects.values())

    def test_new_multiple_objects(self):
        """Test the new method with multiple objects"""
        # Create multiple objects
        user1 = User()
        user2 = User()
        user3 = User()

        # Add the objects to the database
        self.db.new(user1)
        self.db.new(user2)
        self.db.new(user3)
        self.db.save()

        # Retrieve all objects from the database
        objects = self.db.all()

        # Check if all objects are retrieved
        self.assertIn(user1, objects.values())
        self.assertIn(user2, objects.values())
        self.assertIn(user3, objects.values())

    # ...

if __name__ == '__main__':
    unittest.main()
# ...

class TestDBStorage(unittest.TestCase):
    # ...

    def test_all_with_class(self):
        """Test the all method with a specific class"""
        # Create some objects
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        # Add objects to the database
        self.db.new(user)
        self.db.new(state)
        self.db.new(city)
        self.db.new(amenity)
        self.db.new(place)
        self.db.new(review)
        self.db.save()

        # Retrieve objects of a specific class from the database
        objects = self.db.all(cls='User')

        # Check if objects of the specified class are retrieved
        self.assertIn(user, objects.values())
        self.assertNotIn(state, objects.values())
        self.assertNotIn(city, objects.values())
        self.assertNotIn(amenity, objects.values())
        self.assertNotIn(place, objects.values())
        self.assertNotIn(review, objects.values())

    def test_new_multiple_objects(self):
        """Test the new method with multiple objects"""
        # Create multiple objects
        user1 = User()
        user2 = User()
        user3 = User()

        # Add the objects to the database
        self.db.new(user1)
        self.db.new(user2)
        self.db.new(user3)
        self.db.save()

        # Retrieve all objects from the database
        objects = self.db.all()

        # Check if all objects are retrieved
        self.assertIn(user1, objects.values())
        self.assertIn(user2, objects.values())
        self.assertIn(user3, objects.values())

    def test_save(self):
        """Test the save method"""
        # Create an object
        user = User()

        # Add the object to the database
        self.db.new(user)

        # Save the changes
        self.db.save()

        # Retrieve the object from the database
        objects = self.db.all()

        # Check if the object is retrieved
        self.assertIn(user, objects.values())

    def test_delete(self):
        """Test the delete method"""
        # Create an object
        user = User()

        # Add the object to the database
        self.db.new(user)
        self.db.save()

        # Delete the object from the database
        self.db.delete(user)
        self.db.save()

        # Retrieve the object from the database
        objects = self.db.all()

        # Check if the object is deleted
        self.assertNotIn(user, objects.values())

# ...
