"""
Apartment Class (inherits from Property)

This file defines the Apartment class, which is a subclass of the Property class.
An Apartment object represents a residential property with specific attributes such as
the number of bedrooms, bathrooms, and floor number.
"""

from classes.property import Property


class Apartment(Property):
    def __init__(
            self,
            name,
            property_type,
            location,
            price,
            square_footage,
            num_of_bedrooms,
            num_of_bathrooms,
            floor_number):
        """
        Initializes an Apartment object.

        Args:
            name (str): The name of the apartment.
            property_type (str): The type of property (in this case "Apartment").
            location (str): The location of the apartment.
            price (int|float): The price of the apartment.
            square_footage (int|float): The square footage of the apartment.
            num_of_bedrooms (int): The number of bedrooms in the apartment.
            num_of_bathrooms (int): The number of bathrooms in the apartment.
            floor_number (int): The floor number of the apartment.
        """
        super().__init__(name, property_type, location, price, square_footage)
        self.set_num_of_bedrooms(num_of_bedrooms)
        self.set_num_of_bathrooms(num_of_bathrooms)
        self.set_floor_number(floor_number)

    def get_num_of_bedrooms(self):
        """
        Gets the number of bedrooms in the apartment.

        Returns:
            int: The number of bedrooms.
        """
        return self._num_of_bedrooms

    def set_num_of_bedrooms(self, value):
        """
        Sets the number of bedrooms in the apartment.

        Args:
            value (int): The number of bedrooms.

        Raises:
            ValueError: If the value is not an integer or is negative.
        """
        if not isinstance(value, int):
            raise ValueError("The number of bedrooms must be an integer")

        if value < 0:
            self._num_of_bedrooms = 0
        else:
            self._num_of_bedrooms = value

    def get_num_of_bathrooms(self):
        """
        Gets the number of bathrooms in the apartment.

        Returns:
            int: The number of bathrooms.
        """
        return self._num_of_bathrooms

    def set_num_of_bathrooms(self, value):
        """
        Sets the number of bathrooms in the apartment.

        Args:
            value (int): The number of bathrooms.

        Raises:
            ValueError: If the value is not an integer or is negative.
        """
        if not isinstance(value, int):
            raise ValueError(
                f"{__name__}:The number of bathrooms must be an integer")
        if value < 0:
            self._num_of_bathrooms = 0
        else:
            self._num_of_bathrooms = value

    def get_floor_number(self):
        """
        Gets the floor number of the apartment.

        Returns:
            int: The floor number.
        """
        return self._floor_number

    def set_floor_number(self, value):
        """
        Sets the floor number of the apartment.

        Args:
            value (int): The floor number.

        Raises:
            ValueError: If the value is not an integer or is negative.
        """
        if not isinstance(value, int):
            raise ValueError(
                f"{__name__}: The floor number must be an integer")
        if value < 0:
            self._floor_number = 0
        else:
            self._floor_number = value

    def to_dict(self):
        """
        Converts the Apartment object to a dictionary.

        Returns:
            dict: A dictionary representing the Apartment object.
        """
        return {
            "name": self.get_name(),
            "property_type": self.get_property_type(),
            "location": self.get_location(),
            "price": self.get_price(),
            "square_footage": self.get_square_footage(),
            "num_of_bedrooms": self.get_num_of_bedrooms(),
            "num_of_bathrooms": self.get_num_of_bathrooms(),
            "floor_number": self.get_floor_number()
        }
