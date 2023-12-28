"""
Unit Tests for the PropertyManager Class

This file contains unit tests for the PropertyManager class.
It uses the unittest framework to test various methods and functionalities.
"""
import json
import os
import unittest
from classes.property_manager import PropertyManager
from classes.apartment import Apartment
from classes.house import House


class TestPropertyManager(unittest.TestCase):
    """
    Test cases for the PropertyManager class.
    """

    def setUp(self):
        """
        Sets up a sample PropertyManager instance for testing.
        """
        self.property_manager = PropertyManager()

    def test_get_properties(self):
        """
        Tests the get_properties method.
        """
        self.assertEqual(self.property_manager.get_properties(), [])

    def test_read_properties_from_json(self):
        """
        Tests the read_properties_from_json method.
        """
        # Create a temporary JSON file with sample data
        house_dict = {
            "name": "Sample House",
            "property_type": "House",
            "location": "Sample Location",
            "price": 250000,
            "square_footage": 2000,
            "num_of_bedrooms": 3,
            "num_of_bathrooms": 2,
            "num_of_floors": 2
        }
        apartment_dict = {
            "name": "Sample Apartment",
            "property_type": "Apartment",
            "location": "Sample Location",
            "price": 1200,
            "square_footage": 1000,
            "num_of_bedrooms": 2,
            "num_of_bathrooms": 2,
            "floor_number": 5
        }
        commercial_space_dict = {
            "name": "Sample Commercial Space",
            "property_type": "Commercial Space",
            "location": "Sample Location",
            "price": 500000,
            "square_footage": 1500,
            "business_type": "Call Center",
        }
        other_property = {
            "name": "Sample Commercial Space",
            "property_type": "Garage",
            "location": "Sample Location",
            "price": 500000,
            "square_footage": 1500,
            "business_type": "Call Center",
        }
        test_json_data = [
            house_dict,
            apartment_dict,
            commercial_space_dict,
            other_property]
        test_json_path = "test_properties.json"
        with open(test_json_path, "w") as json_file:
            json.dump(test_json_data, json_file)

        # Test reading properties from the created JSON file
        self.property_manager.read_properties_from_json(test_json_path)

        # Check if the properties have been added to the manager
        self.assertEqual(len(self.property_manager.get_properties()), 3)

        # Remove the temporary JSON file
        os.remove(test_json_path)

    def test_read_properties_from_json_invalid_json(self):
        """
        Tests the read_properties_from_json method with an invalid JSON file.
        """
        with self.assertRaises(FileNotFoundError):
            self.property_manager.read_properties_from_json(
                "invalid_file.json")

    def test_read_properties_from_json_missing_property_type(self):
        """
        Tests the read_properties_from_json method with a JSON file missing the "property_type" key.
        """
        # Create a temporary JSON file with missing "property_type"
        invalid_json_data = [
            {"name": "Apt1", "location": "City", "price": 1500, "square_footage": 1200}]
        invalid_json_path = "invalid_properties.json"
        with open(invalid_json_path, "w") as json_file:
            json.dump(invalid_json_data, json_file)

        # Test reading properties from the created JSON file
        with self.assertRaises(Exception):
            self.property_manager.read_properties_from_json(invalid_json_path)

        # Remove the temporary JSON file
        os.remove(invalid_json_path)

    def test_add_property(self):
        """
        Tests the _add_property method.
        """
        apartment = Apartment(
            name="Test Apartment",
            property_type="Apartment",
            location="Test Location",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment)
        self.assertIn(apartment, self.property_manager.get_properties())

    def test_add_property_invalid(self):
        """
        Tests the _add_property method with invalid data.
        """
        apartment_dict = {
            "name": "Sample Apartment",
            "property_type": "Apartment",
            "location": "Sample Location",
            "price": 1200,
            "square_footage": 1000,
            "num_of_bedrooms": 2,
            "num_of_bathrooms": 2,
            "floor_number": 5
        }
        with self.assertRaises(Exception):
            self.property_manager._add_property(apartment_dict)

    def test_filter_by_location(self):
        """
        Tests the filter_by_location method.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)

        filtered_properties = self.property_manager.filter_by_location(
            "Location A")
        self.assertEqual(filtered_properties, [apartment1])

    def test_filter_by_price(self):
        """
        Tests the filter_by_price method.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)

        filtered_properties = self.property_manager.filter_by_price(
            min_price=1600, max_price=2000)
        self.assertEqual(filtered_properties, [apartment2])

    def test_filter_by_price_max_is_none(self):
        """
       Tests the filter_by_price method with the max price being None.
       """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)

        filtered_properties = self.property_manager.filter_by_price(
            min_price=1600, max_price=None)
        self.assertEqual(filtered_properties, [apartment2])

    def test_filter_by_square_footage(self):
        """
        Tests the filter_by_square_footage method.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)

        filtered_properties = self.property_manager.filter_by_square_footage(
            min_square_footage=1300, max_square_footage=1600)
        self.assertEqual(filtered_properties, [apartment2])

    def test_filter_by_square_footage_max_is_none(self):
        """
        Tests the filter_by_square_footage with the max square_footage being None.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)

        filtered_properties = self.property_manager.filter_by_square_footage(
            min_square_footage=1300, max_square_footage=None)
        self.assertEqual(filtered_properties, [apartment2])

    def test_filter_by_property_type(self):
        """
        Tests the filter_by_property_type method.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        house1 = House(
            name="House 1",
            property_type="House",
            location="Location B",
            price=2000,
            square_footage=1800,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            num_of_floors=2,
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(house1)

        filtered_properties = self.property_manager.filter_by_property_type(
            "House")
        self.assertEqual(filtered_properties, [house1])

    def test_sort_properties_by_price(self):
        """
        Tests the sort_properties method. Sorts elements by price.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        house1 = House(
            name="House 1",
            property_type="House",
            location="Location C",
            price=2000,
            square_footage=1800,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            num_of_floors=2
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)
        self.property_manager._add_property(house1)

        sorted_properties = self.property_manager.sort_properties(
            sorting_attribute="price", sorting_type="ascending")
        expected_order = [apartment1, apartment2, house1]
        self.assertEqual(sorted_properties, expected_order)

    def test_sort_properties_by_square_footage(self):
        """
        Tests the sort_properties method. Sorts elements by square footage.
        """
        apartment1 = Apartment(
            name="Apartment 1",
            property_type="Apartment",
            location="Location A",
            price=1500,
            square_footage=1200,
            num_of_bedrooms=2,
            num_of_bathrooms=2,
            floor_number=5
        )
        apartment2 = Apartment(
            name="Apartment 2",
            property_type="Apartment",
            location="Location B",
            price=1800,
            square_footage=1500,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            floor_number=5
        )
        house1 = House(
            name="House 1",
            property_type="House",
            location="Location C",
            price=2000,
            square_footage=1800,
            num_of_bedrooms=3,
            num_of_bathrooms=2,
            num_of_floors=2
        )
        self.property_manager._add_property(apartment1)
        self.property_manager._add_property(apartment2)
        self.property_manager._add_property(house1)

        sorted_properties = self.property_manager.sort_properties(
            sorting_attribute="square_footage", sorting_type="ascending")
        expected_order = [apartment1, apartment2, house1]
        self.assertEqual(sorted_properties, expected_order)


if __name__ == '__main__':
    unittest.main()
