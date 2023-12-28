"""
PropertyManager Class

This file defines the PropertyManager class, which is responsible for managing a list of properties.
It provides methods for reading properties from JSON, adding properties, filtering properties, and sorting properties.
"""

import json
import sys
from classes.property import Property
from classes.apartment import Apartment
from classes.house import House
from classes.commercial_space import CommercialSpace


class PropertyManager:
    def __init__(self):
        """
        Initializes a PropertyManager object with an empty list of properties.
        """
        self._properties = []

    def get_properties(self):
        """
        Gets the list of properties.

        Returns:
            list: The list of properties.
        """
        return self._properties

    def read_properties_from_json(self, path_to_file):
        """
        Reads properties from a JSON file and add them to the list.

        Args:
            path_to_file (str): The path to the JSON file.

        Raises:
            FileNotFoundError: If the path to the JSON file cannot be found.
            Exception: If an error occurs.
        """
        try:
            with open(path_to_file, "r") as json_file:
                data = json.load(json_file)

                for item in data:
                    property_type = item["property_type"].lower()
                    if property_type == "apartment":
                        self._add_property(Apartment(**item))
                    elif property_type == "house":
                        self._add_property(House(**item))
                    elif property_type == "commercial space":
                        self._add_property(CommercialSpace(**item))
                    else:
                        print(
                            f"{__name__}: Property type {property_type} not supported",
                            file=sys.stderr)
        except FileNotFoundError as e:
            print(
                f"{__name__}: File called {path_to_file} could not be found!",
                file=sys.stderr)
            raise e
        except Exception as e:
            print(f"{__name__}: An error occurred: {e}", file=sys.stderr)
            raise e

    def _add_property(self, property_to_add):
        """
        Adds a property to the list. (protected method)

        Args:
            property_to_add (Property): The property to add.

        Raises:
            Exception: If the given object is not an instance of Property.
        """
        if not (isinstance(property_to_add, Property)):
            raise Exception(f"{__name__}: Cannot add property")

        self._properties.append(property_to_add)

    def filter_by_location(self, location):
        """
        Filters properties by location.

        Args:
            location (str): The location to filter by.

        Returns:
            list: The filtered list of properties.
        """
        return [prop for prop in self._properties if prop.get_location().lower()
                == location.lower()]

    def filter_by_price(self, min_price=0, max_price=None):
        """
        Filters properties by price range.

        Args:
            min_price (int): The minimum price.
            max_price (int): The maximum price.

        Returns:
            list: The filtered list of properties.
        """
        if max_price is None:
            max_price = max(prop.get_price() for prop in self._properties)

        return [prop for prop in self._properties if min_price <=
                prop.get_price() <= max_price]

    def filter_by_square_footage(
            self,
            min_square_footage=0,
            max_square_footage=None):
        """
        Filters properties by square footage range.

        Args:
            min_square_footage (int): The minimum square footage.
            max_square_footage (int): The maximum square footage.

        Returns:
            list: The filtered list of properties.
        """
        if max_square_footage is None:
            max_square_footage = max(prop.get_square_footage()
                                     for prop in self._properties)

        return [prop for prop in self._properties if min_square_footage <=
                prop.get_square_footage() <= max_square_footage]

    def filter_by_property_type(self, property_type):
        """
        Filters properties by property type.

        Args:
            property_type (str): The property type to filter by.

        Returns:
            list: The filtered list of properties.
        """
        return [prop for prop in self._properties if prop.get_property_type(
        ).lower() == property_type.lower()]

    def sort_properties(self, sorting_attribute, sorting_type):
        """
        Sorts properties based on the given attribute and sorting type.

        Args:
            sorting_attribute (str): The attribute to sort by ("price" or "square_footage").
            sorting_type (str): The sorting type ("ascending" or "descending").

        Returns:
            list: The sorted list of properties.
        """

        reverse = True if sorting_type == "descending" else False

        if sorting_attribute == "price":
            return sorted(
                self._properties,
                key=lambda prop: prop.get_price(),
                reverse=reverse)
        else:
            return sorted(
                self._properties,
                key=lambda prop: prop.get_square_footage(),
                reverse=reverse)
