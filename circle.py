import math


def area(r):
    if r < 0:
        raise ValueError("Radius can't have a negative value")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise ValueError("Radius can't have a negative value")
    return 2 * math.pi * r
