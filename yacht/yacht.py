from functools import partial

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
def check_yacht_yacht(dice):
    roll_score = score_calc(dice)
    return 50 if sum(map((5).__eq__, roll_score.values())) else 0


def score_calc(dice):
    dice_count = {}
    for i in range(1, 7):
        dice_count[i] = dice.count(i)
    return dice_count


def standard_score(dice, category_calc):
    roll_score = score_calc(dice)
    return category_calc * roll_score[category_calc]


def full_house(dice):
    roll_score = score_calc(dice)

    three_of_a_kind = 0
    two_of_a_kind = 0
    for k, v in roll_score.items():
        if v == 3:
            three_of_a_kind += k * v
        if v == 2:
            two_of_a_kind += k * v
    return three_of_a_kind + two_of_a_kind if three_of_a_kind > 0 and two_of_a_kind > 0 else 0


def check_four_of_a_kind(dice, category_calc=4):
    roll_score = score_calc(dice)

    four_of_a_kind = 0
    for k, v in roll_score.items():
        if v >= category_calc:
            four_of_a_kind = k * category_calc
    return four_of_a_kind


def choisir(dice):
    roll_score = score_calc(dice)
    return sum(k*v for k, v in roll_score.items())


def straight(dice, reversed_order):
    roll_score = score_calc(dice)

    if reversed_order:
        sorted_roll_score = list(reversed(sorted(roll_score.keys())))
    else:
        sorted_roll_score = list(sorted(roll_score.keys()))

    run_ctr = 0
    for k in sorted_roll_score:
        v = roll_score[k]
        if v in [1, 2]:
            run_ctr += 1
        if v == 0:
            break
    return 30 if run_ctr == 5 else 0


YACHT = check_yacht_yacht
ONES = partial(standard_score, category_calc=1)
TWOS = partial(standard_score, category_calc=2)
THREES = partial(standard_score, category_calc=3)
FOURS = partial(standard_score, category_calc=4)
FIVES = partial(standard_score, category_calc=5)
SIXES = partial(standard_score, category_calc=6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = check_four_of_a_kind
LITTLE_STRAIGHT = partial(straight, reversed_order=False)
BIG_STRAIGHT = partial(straight, reversed_order=True)
CHOICE = choisir


def score(dice, category):
    return category(dice)
