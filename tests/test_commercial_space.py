"""
Unit Tests for the CommercialSpace Class

This file contains unit tests for the CommercialSpace class.
It uses the unittest framework to test various methods and functionalities.
"""

import unittest
from classes.commercial_space import CommercialSpace


class TestCommercialSpace(unittest.TestCase):
    """
    Test cases for the CommercialSpace class.
    """

    def setUp(self):
        """
        Sets up a sample CommercialSpace instance for testing.
        """
        self.commercial_space = CommercialSpace(
            name="Sample Commercial Space",
            property_type="Commercial Space",
            location="Sample Location",
            price=500000,
            square_footage=1500,
            business_type="Call Center"
        )

    def test_get_business_type(self):
        """
        Tests the get_business_type method.
        """
        self.assertEqual(
            self.commercial_space.get_business_type(),
            "Call Center")

    def test_set_business_type(self):
        """
        Tests the set_business_type method.
        """
        self.commercial_space.set_business_type("Healthcare")
        self.assertEqual(
            self.commercial_space.get_business_type(),
            "Healthcare")

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        expected_dict = {
            "name": "Sample Commercial Space",
            "property_type": "Commercial Space",
            "location": "Sample Location",
            "price": 500000,
            "square_footage": 1500,
            "business_type": "Call Center",
        }
        self.assertEqual(self.commercial_space.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
