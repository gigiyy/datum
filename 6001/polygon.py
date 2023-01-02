import math


def polysum(n, s):
    """
    Input: n int - number of sides of a regular polygon, s number - length of each side
    Returns the sum of area and square of perimeter, rounded to 4th digit
    """
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter = n * s

    return round(area + perimeter ** 2, 4)
