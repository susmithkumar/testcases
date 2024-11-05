import math

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(math.radians(x))

def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(math.radians(x))

def tan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tan(math.radians(x))

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)

def log(x):
    if x <= 0:
        raise ValueError("logarithm undefined for non-positive numbers")
    return math.log10(x)

def exp(x):
    return math.exp(x)

def asin(x):
    if not isinstance(x, (int, float)) or not (-1 <= x <= 1):
        raise ValueError("Input for asin must be between -1 and 1")
    return math.degrees(math.asin(x))