#!/usr/bin/python3
"""A square represented by a Square class"""


class Square:
    """
    Represents a square.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        area(): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (float or int, optional): The size of
            the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality comparison operator (==).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparison operator (!=).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Greater than comparison operator (>).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal to comparison operator (>=).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Less than comparison operator (<).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal to comparison operator (<=).

        Args:
            other: The object to compare with.

        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
