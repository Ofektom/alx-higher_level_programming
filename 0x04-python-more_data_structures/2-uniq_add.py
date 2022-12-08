#!/usr/bin/python3
# 2-uniq_add.py
# Ofofonono Okpoho

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    result = 0
    for  num in set(my_list):
        result += num
    return result
