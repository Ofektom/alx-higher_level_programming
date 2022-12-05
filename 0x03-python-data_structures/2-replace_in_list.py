#!/usr/bin/python3
# 2-replace_in_list.py
# Ofofonono Okpoho

def replace_in_list(my_list, idx, element):
    """replace element of index in a list"""
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
