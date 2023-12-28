"""
Unit Tests for the Property Class (tested using the derived Apartment Class)

This file contains unit tests for the Property and Apartment classes.
It uses the unittest framework for testing various methods and functionalities.
"""

import unittest
from classes.property import Property
from classes.apartment import Apartment


class TestProperty(unittest.TestCase):
    """
    Test cases for the Property class.
    """

    def setUp(self):
        """
        Sets up a sample Apartment instance for testing.
        """
        self.property = Apartment(
            name="Sample Property",
            property_type="Apartment",
            location="Sample Location",
            price=100000,
            square_footage=1500,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )

    def test_generate_uuid(self):
        """
        Tests the generate_uuid function.
        """
        # Tests if the generate_uuid function returns a string
        uuid_value = Property.generate_uuid()
        self.assertIsInstance(uuid_value, str)

    def test_get_name(self):
        """
        Tests the get_name method.
        """
        self.assertEqual(self.property.get_name(), "Sample Property")

    def test_get_id(self):
        """
        Tests the get_id method.
        """
        self.assertEqual(len(self.property.get_id()), 36)

    def test_set_name(self):
        """
        Tests the set_name method.
        """
        self.property.set_name("New Name")
        self.assertEqual(self.property.get_name(), "New Name")

    def test_get_property_type(self):
        """
        Tests the get_property_type method.
        """
        self.assertEqual(self.property.get_property_type(), "Apartment")

    def test_set_property_type_valid(self):
        """
        Tests the set_property_type method with a valid property type.
        """
        self.property.set_property_type("House")
        self.assertEqual(self.property.get_property_type(), "House")

    def test_set_property_type_invalid(self):
        """
        Tests the set_property_type method with an invalid property type.
        """
        with self.assertRaises(ValueError):
            self.property.set_property_type("Invalid Type")

    def test_get_location(self):
        """
        Tests the get_location method.
        """
        self.assertEqual(self.property.get_location(), "Sample Location")

    def test_set_location(self):
        """
        Tests the set_location method.
        """
        self.property.set_location("New Location")
        self.assertEqual(self.property.get_location(), "New Location")

    def test_get_price(self):
        """
        Tests the get_price method.
        """
        self.assertEqual(self.property.get_price(), 100000)

    def test_set_price_valid(self):
        """
        Tests the set_price method with a valid price.
        """
        self.property.set_price(150000)
        self.assertEqual(self.property.get_price(), 150000)

    def test_price_negative(self):
        """
        Tests the set_price method with a negative square footage.
        """
        self.property.set_price(-500)
        self.assertEqual(self.property.get_price(), 0)

    def test_set_price_invalid(self):
        """
        Tests the set_price method with an invalid price.
        """
        with self.assertRaises(ValueError):
            self.property.set_price("Invalid Price")

    def test_get_square_footage(self):
        """
        Tests the get_square_footage method.
        """
        self.assertEqual(self.property.get_square_footage(), 1500)

    def test_set_square_footage_valid(self):
        """
        Tests the set_square_footage method with a valid square footage.
        """
        self.property.set_square_footage(2000)
        self.assertEqual(self.property.get_square_footage(), 2000)

    def test_set_square_footage_invalid(self):
        """
        Tests the set_square_footage method with an invalid square footage.
        """
        with self.assertRaises(ValueError):
            self.property.set_square_footage("Invalid Footage")

    def test_set_square_footage_negative(self):
        """
        Tests the set_square_footage method with a negative square footage.
        """
        self.property.set_square_footage(-500)
        self.assertEqual(self.property.get_square_footage(), 0)


if __name__ == '__main__':
    unittest.main()
