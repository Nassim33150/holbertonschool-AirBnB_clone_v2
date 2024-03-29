#!/usr/bin/python3
"""Test unittest for class Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_args(self):
        """Test initialization of Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test unittest for class Review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_args(self):
        """Test initialization of Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_text(self):
        """Test text attribute of Review class"""
        review = Review()
        review.text = "Great place!"
        self.assertEqual(review.text, "Great place!")

    def test_place_id(self):
        """Test place_id attribute of Review class"""
        review = Review()
        review.place_id = "123"
        self.assertEqual(review.place_id, "123")

    def test_user_id(self):
        """Test user_id attribute of Review class"""
        review = Review()
        review.user_id = "456"
        self.assertEqual(review.user_id, "456")


if __name__ == '__main__':
    unittest.main()
