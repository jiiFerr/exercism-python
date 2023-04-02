def square(number):

    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    square_grains = 1
    for i in range(2, number+1):
        square_grains = square_grains * 2

    return square_grains


def total():

    total_grains = 1
    for i in range(2, 66):
        total_grains = total_grains * 2

    total_grains = total_grains - 1

    return total_grains
