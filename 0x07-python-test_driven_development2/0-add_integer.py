#!/usr/bin/python3

def add_integer(a, b=98):
    """ returns the summation of 2 integers or float type"""
    if type(a) not in [int, float]:
        raise TypeError("a should be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b should be an integer")
    return int(a+b)
