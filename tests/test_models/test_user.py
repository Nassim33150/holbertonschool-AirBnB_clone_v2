#!/usr/bin/python3
"""Test unittest for class User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_args(self):
        """Test initialization with arguments"""
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_default_values(self):
        """Test initialization with default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""Test unittest for class User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_args(self):
        """Test initialization with arguments"""
        user = User(email="test@example.com", password="password",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_default_values(self):
        """Test initialization with default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_email_column(self):
        """Test email column"""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(user.email, "")

    def test_password_column(self):
        """Test password column"""
        user = User()
        self.assertEqual(type(user.password), str)
        self.assertEqual(user.password, "")

    def test_first_name_column(self):
        """Test first_name column"""
        user = User()
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(user.first_name, "")

    def test_last_name_column(self):
        """Test last_name column"""
        user = User()
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
