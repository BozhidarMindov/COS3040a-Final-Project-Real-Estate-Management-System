"""
Unit Tests for the Apartment Class

This file contains unit tests for the Apartment class.
It uses the unittest framework to test various methods and functionalities.
"""

import unittest
from classes.apartment import Apartment


class TestApartment(unittest.TestCase):
    """
    Test cases for the Apartment class.
    """

    def setUp(self):
        """
        Sets up a sample Apartment instance for testing.
        """
        self.apartment = Apartment(
            name="Sample Apartment",
            property_type="Apartment",
            location="Sample Location",
            price=1200,
            square_footage=1000,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )

    def test_get_num_of_bedrooms(self):
        """
        Tests the get_num_of_bedrooms method.
        """
        self.assertEqual(self.apartment.get_num_of_bedrooms(), 2)

    def test_set_num_of_bedrooms_valid(self):
        """
        Tests the set_num_of_bedrooms method with a valid value.
        """
        self.apartment.set_num_of_bedrooms(3)
        self.assertEqual(self.apartment.get_num_of_bedrooms(), 3)

    def test_set_num_of_bedrooms_negative(self):
        """
        Tests the set_num_of_bedrooms method with a negative value.
        """
        self.apartment.set_num_of_bedrooms(-1)
        self.assertEqual(self.apartment.get_num_of_bedrooms(), 0)

    def test_set_num_of_bedrooms_invalid_type(self):
        """
        Tests the set_num_of_bedrooms method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.apartment.set_num_of_bedrooms("invalid")

    def test_get_num_of_bathrooms(self):
        """
        Tests the get_num_of_bathrooms method.
        """
        self.assertEqual(self.apartment.get_num_of_bathrooms(), 2)

    def test_set_num_of_bathrooms_valid(self):
        """
        Tests the set_num_of_bathrooms method with a valid value.
        """
        self.apartment.set_num_of_bathrooms(3)
        self.assertEqual(self.apartment.get_num_of_bathrooms(), 3)

    def test_set_num_of_bathrooms_negative(self):
        """
        Tests the set_num_of_bathrooms method with a negative value.
        """
        self.apartment.set_num_of_bathrooms(-1)
        self.assertEqual(self.apartment.get_num_of_bathrooms(), 0)

    def test_set_num_of_bathrooms_invalid_type(self):
        """
        Tests the set_num_of_bathrooms method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.apartment.set_num_of_bathrooms("invalid")

    def test_get_floor_number(self):
        """
        Tests the get_floor_number method.
        """
        self.assertEqual(self.apartment.get_floor_number(), 5)

    def test_set_floor_number_valid(self):
        """
        Tests the set_floor_number method with a valid value.
        """
        self.apartment.set_floor_number(3)
        self.assertEqual(self.apartment.get_floor_number(), 3)

    def test_set_floor_number_negative(self):
        """
        Tests the set_floor_number method with a negative value.
        """
        self.apartment.set_floor_number(-1)
        self.assertEqual(self.apartment.get_floor_number(), 0)

    def test_set_floor_number_invalid_type(self):
        """
        Tests the set_floor_number method with an invalid type.
        """
        with self.assertRaises(ValueError):
            self.apartment.set_floor_number("invalid")

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        expected_dict = {
            "name": "Sample Apartment",
            "property_type": "Apartment",
            "location": "Sample Location",
            "price": 1200,
            "square_footage": 1000,
            "num_of_bedrooms": 2,
            "num_of_bathrooms": 2,
            "floor_number": 5
        }
        self.assertEqual(self.apartment.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
