#!/usr/bin/puthon3

class Square:
    """class of the square of any given number"""
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int):
            try:
                return self.__size
            except TypeError:
                return "size must be an integer"
        if size >= 0:
            try:
                return self.__size
            except ValueError:
                return "size must be >= 0"
