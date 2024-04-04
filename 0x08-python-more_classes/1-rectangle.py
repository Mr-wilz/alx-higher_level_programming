#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    - __width (int).
    - __height (int).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Parameters:
        - width (int): Optional width of the rectangle.
        - height (int): Optional height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.

        Returns:
        - int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Parameters:
        - value (int): The width to set.

        Raises:
        - TypeError: If the width is not an integer.
        - ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.

        Returns:
        - int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Parameters:
        - value (int): The height to set.

        Raises:
        - TypeError: If the height is not an integer.
        - ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
