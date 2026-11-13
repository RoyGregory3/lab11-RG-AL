"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        print("Cannot take square root of negative number.")
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        print("Arguments contain incompatible data types.")
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a
def logarithm(a, b):
    if b == 0:
        raise ValueError("Log of zero is undefined.")
    return math.log(b, a)
def exponent(a, b):
    return a ** b



