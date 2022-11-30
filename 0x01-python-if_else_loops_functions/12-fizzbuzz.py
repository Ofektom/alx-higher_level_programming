#!/usr/bin/python3
# 12-fizzbuzz.py
# Ofofonono Okpoho

def fizzbuzz():
    """print multiples of 3, 5 and both"""
    for number in range(1, 101):
        if number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        elif number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        else:
            print("{} ".format(number), end="")
