# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
bake_time_remaining = 0
preparation_time_in_minutes = 0
elapsed_time_in_minutes = 0
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):

    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    if elapsed_bake_time > EXPECTED_BAKE_TIME:
        print("Lasagne gonnae burn!")
        raise ValueError

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int):
    """ Calculate the Preparation time in minutes.

    :param: number_of_layers: The Number of Layers of Lasagne.
    :return: preparation_time_in_minutes: The total preparation time in minutes
                                            for x number of layers of lasagne.

    Each Layer of Lasagne, takes a defined amount of time in minutes to prepare.
    """
    preparation_time_in_minutes = PREPARATION_TIME * number_of_layers
    return preparation_time_in_minutes


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """ Calculate the elapsed time in Minutes

    :param number_of_layers: The number of layers of Lasagne.
    :param elapsed_bake_time:The number of minutes the lasagna has been baking
    :return:
    """

    elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    return elapsed_time_in_minutes
