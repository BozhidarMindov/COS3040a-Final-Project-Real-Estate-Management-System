"""
Property Class

This file defines the abstract Property class, which serves as the base class for
different types of properties (House, Apartment, Commercial Space).
"""

import uuid
from abc import ABC, abstractmethod


class Property(ABC):
    def __init__(self, name, property_type, location, price, square_footage):
        """
        Initializes a Property object.

        Args:
            name (str): The name of the property.
            property_type (str): The type of property (e.g., "House", "Apartment", "Commercial Space").
            location (str): The location of the property.
            price (int|float): The price of the property.
            square_footage (int|float): The square footage of the property.
        """
        self.set_name(name)
        self.set_property_type(property_type)
        self.set_location(location)
        self.set_price(price)
        self.set_square_footage(square_footage)
        self._id = self.generate_uuid()

    def get_id(self):
        """
        Gets the ID of the property.

        Returns:
            str: The ID of the property.
        """
        return self._id

    def get_name(self):
        """
        Gets the name of the property.

        Returns:
            str: The name of the property.
        """
        return self._name

    def set_name(self, name):
        """
        Sets the name of the property.

        Args:
            name (str): The name of the property.
        """
        self._name = name

    def get_property_type(self):
        """
        Gets the type of the property.

        Returns:
            str: The type of the property.
        """
        return self._property_type

    def set_property_type(self, value):
        """
        Set the type of the property.

        Args:
            value (str): The type of the property.

        Raises:
            ValueError: If the provided property type is not valid.
        """
        if value.title() not in ["House", "Apartment", "Commercial Space"]:
            raise ValueError(
                f"{__name__}: Property Type must be House, Apartment or Commercial Space")

        self._property_type = value.title()

    def get_location(self):
        """
        Gets the location of the property.

        Returns:
            str: The location of the property.

        """
        return self._location

    def set_location(self, value):
        """
        Sets the location of the property.

        Args:
            value (str): The location of the property.
        """
        self._location = value

    def get_price(self):
        """
        Gets the price of the property.

        Returns:
            int|float: The price of the property.
        """
        return self._price

    def set_price(self, value):
        """
        Sets the price of the property.

        Args:
            value (int|float): The price of the property.

        Raises:
            ValueError: If the provided price is not a valid number.
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{__name__}: Price must be either int or float")

        if value < 0:
            self._price = 0
        else:
            self._price = value

    def get_square_footage(self):
        """
        Gets the square footage of the property.

        Returns:
            int|float: The square footage of the property.
        """
        return self._square_footage

    def set_square_footage(self, value):
        """
        Sets the square footage of the property.

        Args:
            value (int|float): The square footage of the property.

        Raises:
            ValueError: If the provided square footage is not a valid number.
        """
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"{__name__}: Square footage must be either int or float")

        if value < 0:
            self._square_footage = 0
        else:
            self._square_footage = value

    @staticmethod
    def generate_uuid():
        """
        Generates a UUID (Universally Unique Identifier).

        Returns:
            str: A string representing the generated UUID.
        """
        return str(uuid.uuid4())

    @abstractmethod
    def to_dict(self):
        """
        Converts the Property object to a dictionary.

        This method must be implemented by concrete subclasses.

        Returns:
            dict: A dictionary representing the Property object.
        """

        pass
