import math
import unittest


def calculate_square_root():
    number = float(
        input("Enter a number: ")
    )  # using int function only limit you to whole numbers ,choose float instead
    sqrt_number = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_number}")


def multiply(a, b):
    return a * b


def remove_vowels(string):
    vowels = "aeiouAEIOU"
