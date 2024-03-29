#!/usr/bin/python3
"""Test unittest for class Amenity"""
import unittest
from models.amenity import Amenity
from models.place import Place


class TestAmenity(unittest.TestCase):
    """Test cases for class Amenity"""

    def test_args(self):
        """Test initialization of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test unittest for class Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for class Amenity"""

    def test_args(self):
        """Test initialization of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name(self):
        """Test setting the name attribute"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_place_amenities(self):
        """Test place_amenities relationship"""
        amenity = Amenity()
        self.assertEqual(amenity.place_amenities, [])

        place1 = Place()
        place2 = Place()
        amenity.place_amenities.append(place1)
        amenity.place_amenities.append(place2)

        self.assertEqual(len(amenity.place_amenities), 2)
        self.assertIn(place1, amenity.place_amenities)
        self.assertIn(place2, amenity.place_amenities)


if __name__ == '__main__':
    unittest.main()
