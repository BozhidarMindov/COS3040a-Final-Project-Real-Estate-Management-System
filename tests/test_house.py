"""
Unit Tests for the House Class

This file contains unit tests for the House class.
It uses the unittest framework to test various methods and functionalities.
"""

import unittest
from classes.house import House


class TestHouse(unittest.TestCase):
    """
    Test cases for the House class.
    """

    def setUp(self):
        """
        Sets up a sample House instance for testing.
        """
        self.house = House(
            name="Sample House",
            property_type="House",
            location="Sample Location",
            price=250000,
            square_footage=2000,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            num_of_floors=2
        )

    def test_get_num_of_bedrooms(self):
        """
        Tests the get_num_of_bedrooms method.
        """
        self.assertEqual(self.house.get_num_of_bedrooms(), 3)

    def test_set_num_of_bedrooms_valid(self):
        """
        Tests the set_num_of_bedrooms method with a valid value.
        """
        self.house.set_num_of_bedrooms(4)
        self.assertEqual(self.house.get_num_of_bedrooms(), 4)

    def test_set_num_of_bedrooms_negative(self):
        """
        Tests the set_num_of_bedrooms method with a negative value.
        """
        self.house.set_num_of_bedrooms(-1)
        self.assertEqual(self.house.get_num_of_bedrooms(), 0)

    def test_set_num_of_bedrooms_invalid_type(self):
        """
        Tests the set_num_of_bedrooms method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.house.set_num_of_bedrooms("invalid")

    def test_get_num_of_bathrooms(self):
        """
        Tests the get_num_of_bathrooms method.
        """
        self.assertEqual(self.house.get_num_of_bathrooms(), 2)

    def test_set_num_of_bathrooms_valid(self):
        """
        Tests the set_num_of_bathrooms method with a valid value.
        """
        self.house.set_num_of_bathrooms(3)
        self.assertEqual(self.house.get_num_of_bathrooms(), 3)

    def test_set_num_of_bathrooms_negative(self):
        """
        Tests the set_num_of_bathrooms method with a negative value.
        """
        self.house.set_num_of_bathrooms(-1)
        self.assertEqual(self.house.get_num_of_bathrooms(), 0)

    def test_set_num_of_bathrooms_invalid_type(self):
        """
        Tests the set_num_of_bathrooms method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.house.set_num_of_bathrooms("invalid")

    def test_get_num_of_floors(self):
        """
        Tests the get_num_of_floors method.
        """
        self.assertEqual(self.house.get_num_of_floors(), 2)

    def test_set_num_of_floors_valid(self):
        """
        Tests the set_num_of_floors method with a valid value.
        """
        self.house.set_num_of_floors(3)
        self.assertEqual(self.house.get_num_of_floors(), 3)

    def test_set_num_of_floors_negative(self):
        """
        Tests the set_num_of_floors method with a negative value.
        """
        self.house.set_num_of_floors(-1)
        self.assertEqual(self.house.get_num_of_floors(), 0)

    def test_set_num_of_floors_invalid_type(self):
        """
        Tests the set_num_of_floors method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.house.set_num_of_floors("invalid")

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        expected_dict = {
            "name": "Sample House",
            "property_type": "House",
            "location": "Sample Location",
            "price": 250000,
            "square_footage": 2000,
            "num_of_bedrooms": 3,
            "num_of_bathrooms": 2,
            "num_of_floors": 2
        }
        self.assertEqual(self.house.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
