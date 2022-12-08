#!/usr/bin/python3
# 0-square_matrix_simple.py
# Ofofonono Okpoho

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    func = lambda x: x**2
    return [list(map(func, row)) for row in matrix]
