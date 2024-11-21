def area(a, h):
    if (a < 0) or (h < 0):
        raise ValueError("Length can't have a negative value")
    return (a * h) / 2


def perimeter(a, b, c):
    if (a <= 0) or (b <= 0) or (c <= 0):
        raise ValueError("Length can't have a negative/zero value")
    return a + b + c
