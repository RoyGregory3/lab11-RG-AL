import math

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

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def exponent(a, b):
    return a ** b



