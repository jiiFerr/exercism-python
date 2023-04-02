import numbers
import math

def score(x: int, y: int):
    """
    Deduces a dartboard score, based on input Cartesian Coordinates

    :param x: Cartesian X Coordinate of dart
    :param y: Cartesian Y Coordinate of dart
    :return: The Dartboard Score - 0,1,5,10.
    """

    if not (isinstance(x, numbers.Number) and isinstance(y, numbers.Number)):
        raise ValueError("X and Y Coordinates need to be numbers.")

    # x^2 + y^2 = radius^2
    dart_radial = math.sqrt(x ** 2 + y ** 2)

    rtn_score = 0
    if dart_radial <= 1:
        rtn_score = 10
    elif 1 < dart_radial <= 5:
        rtn_score = 5
    elif 5 < dart_radial <= 10:
        rtn_score = 1

    return rtn_score
