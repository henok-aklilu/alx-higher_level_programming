#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """This class is a squeleton for Square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size**2
