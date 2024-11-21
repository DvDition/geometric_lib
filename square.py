def area(a):
    if a < 0:
        raise ValueError("Length can't have a negative value")
    return a * a


def perimeter(a):
    if a < 0:
        raise ValueError("Length can't have a negative value")
    return 4 * a
