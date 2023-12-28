"""
CommercialSpace Class (inherits from Property)

This file defines the CommercialSpace class, which is a subclass of the Property class.
A CommercialSpace object represents a commercial property with additional attributes such as
the type of business operating in the space.
"""

from classes.property import Property


class CommercialSpace(Property):
    def __init__(
            self,
            name,
            property_type,
            location,
            price,
            square_footage,
            business_type):
        """
        Initializes a CommercialSpace object.

        Args:
            name (str): The name of the property.
            property_type (str): The type of property (in this case "Commercial Space").
            location (str): The location of the property.
            price (int|float): The price of the property.
            square_footage (int|float): The square footage of the property.
            business_type (str): The type of business operating in the commercial space.
        """
        super().__init__(name, property_type, location, price, square_footage)
        self.set_business_type(business_type)

    def get_business_type(self):
        """
        Gets the type of business operating in the commercial space.

        Returns:
            str: The business type.
        """
        return self._business_type

    def set_business_type(self, value):
        """
        Sets the type of business operating in the commercial space.

        Args:
            value (str): The business type.
        """
        self._business_type = value

    def to_dict(self):
        """
        Converts the CommercialSpace object to a dictionary.

        Returns:
            dict: A dictionary representing the CommercialSpace object.
        """
        return {
            "name": self.get_name(),
            "property_type": self.get_property_type(),
            "location": self.get_location(),
            "price": self.get_price(),
            "square_footage": self.get_square_footage(),
            "business_type": self.get_business_type(),
        }
