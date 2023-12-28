"""
House Class (inherits from Property)

This module defines the House class, which is a subclass of the Property class.
A House object represents a residential property with additional attributes such as
the number of bedrooms, bathrooms, and floors.
"""

from classes.property import Property


class House(Property):
    def __init__(
            self,
            name,
            property_type,
            location,
            price,
            square_footage,
            num_of_bedrooms,
            num_of_bathrooms,
            num_of_floors):
        """
        Initializes a House object.

        Args:
            name (str): The name of the property.
            property_type (str): The type of property (in this case "House").
            location (str): The location of the property.
            price (int|float): The price of the property.
            square_footage (int|float): The square footage of the property.
            num_of_bedrooms (int): The number of bedrooms in the house.
            num_of_bathrooms (int): The number of bathrooms in the house.
            num_of_floors (int): The number of floors in the house.

        """
        super().__init__(name, property_type, location, price, square_footage)
        self.set_num_of_bedrooms(num_of_bedrooms)
        self.set_num_of_bathrooms(num_of_bathrooms)
        self.set_num_of_floors(num_of_floors)

    def get_num_of_bedrooms(self):
        """
        Gets the number of bedrooms in the house.

        Returns:
            int: The number of bedrooms.
        """
        return self._num_of_bedrooms

    def set_num_of_bedrooms(self, value):
        """
        Sets the number of bedrooms in the house.

        Args:
            value (int): The number of bedrooms.

        Raises:
            ValueError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError(
                f"{__name__}: The number of bedrooms must be an integer")

        if value < 0:
            self._num_of_bedrooms = 0
        else:
            self._num_of_bedrooms = value

    def get_num_of_bathrooms(self):
        """
        Gets the number of bathrooms in the house.

        Returns:
            int: The number of bathrooms.
        """
        return self._num_of_bathrooms

    def set_num_of_bathrooms(self, value):
        """
        Sets the number of bathrooms in the house.

        Args
            value (int): The number of bathrooms.

        Raises:
            ValueError: If the provided value is not an integer.

        """
        if not isinstance(value, int):
            raise ValueError(
                f"{__name__}: The number of bathrooms must be an integer")

        if value < 0:
            self._num_of_bathrooms = 0
        else:
            self._num_of_bathrooms = value

    def get_num_of_floors(self):
        """
        Gets the number of floors in the house.

        Returns:
            int: The number of floors.
        """
        return self._num_of_floors

    def set_num_of_floors(self, value):
        """
        Sets the number of floors in the house.

        Args:
            value (int): The number of floors.

        Raises:
            ValueError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError(
                f"{__name__}: The number of floors must be an integer")

        if value < 0:
            self._num_of_floors = 0
        else:
            self._num_of_floors = value

    def to_dict(self):
        """
        Converts the House object to a dictionary.

        Returns:
            dict: A dictionary representing the House object.
        """
        return {
            "name": self.get_name(),
            "property_type": self.get_property_type(),
            "location": self.get_location(),
            "price": self.get_price(),
            "square_footage": self.get_square_footage(),
            "num_of_bedrooms": self.get_num_of_bedrooms(),
            "num_of_bathrooms": self.get_num_of_bathrooms(),
            "num_of_floors": self.get_num_of_floors()
        }
