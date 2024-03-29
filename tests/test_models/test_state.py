#!/usr/bin/python3
"""Test unittest for class State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """blablabla"""

    def test_args(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test unittest for class State"""
import unittest
from models.state import State
from models.city import City
from models import storage
import os


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up test environment"""
        self.state = State()

    def tearDown(self):
        """Clean up test environment"""
        del self.state

    def test_name_default_value(self):
        """Test default value of name attribute"""
        self.assertEqual(self.state.name, "")

    def test_cities_property(self):
        """Test cities property"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertEqual(self.state.cities, [])
        else:
            city1 = City(state_id=self.state.id)
            city2 = City(state_id=self.state.id)
            storage.new(city1)
            storage.new(city2)
            storage.save()
            cities = self.state.cities
            self.assertIn(city1, cities)
            self.assertIn(city2, cities)

if __name__ == '__main__':
    unittest.main()
