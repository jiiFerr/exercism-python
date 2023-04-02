def equilateral(sides: list):
    sides.sort()
    if sides[0] <= 0:
        return False

    return True if sides[0] == sides[1] == sides[2] else False


def isosceles(sides: list):
    sides.sort()
    if sides[0] <= 0:
        return False

    if inequality_violation(sides):
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (a == b and b != c) or (a != b and b == c):
        return True
    elif equilateral(sides):
        return True
    else:
        return False


def scalene(sides: list):
    sides.sort()
    if inequality_violation(sides):
        return False
    return True if sides[0] != sides[1] != sides[2] else False


def inequality_violation(sides: list):
    return True if not sides[2] <= sides[0] + sides[1] else False

