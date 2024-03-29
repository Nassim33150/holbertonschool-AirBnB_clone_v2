#!/usr/bin/python3
"""Test unittest for class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for class Place"""

    def test_args(self):
        """Test initialization with arguments"""
        place = Place(city_id="123", user_id="456", name="Test Place",
                      description="This is a test place",
                      number_rooms=2, number_bathrooms=1,
                      max_guest=4, price_by_night=100,
                      latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["amenity1", "amenity2"])

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "This is a test place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test unittest for class Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for class Place"""

    def test_args(self):
        """Test initialization with arguments"""
        place = Place(city_id="123", user_id="456", name="Test Place",
                      description="This is a test place",
                      number_rooms=2, number_bathrooms=1,
                      max_guest=4, price_by_night=100,
                      latitude=37.7749, longitude=-122.4194,
                      amenity_ids=["amenity1", "amenity2"])

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "This is a test place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_attributes(self):
        """Test attributes of Place"""
        place = Place()

        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_default_values(self):
        """Test default values of Place"""
        place = Place()

        self.assertEqual(place.city_id, None)
        self.assertEqual(place.user_id, None)
        self.assertEqual(place.name, None)
        self.assertEqual(place.description, None)
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, None)
        self.assertEqual(place.longitude, None)
        self.assertEqual(place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
