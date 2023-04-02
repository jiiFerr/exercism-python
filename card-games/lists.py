import math


def get_rounds(number: int):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list, rounds_2: list):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand: list):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand: list):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    hand_median = hand[math.trunc((len(hand) - 1) / 2)]
    approx_avg = (hand[0] + hand[-1]) / 2

    return bool(card_average(hand) in [approx_avg, hand_median])


def average_even_is_average_odd(hand: list):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return bool( sum(hand[::2]) / len(hand[::2]) == sum(hand[1::2]) / len(hand[1::2]) )

def maybe_double_last(hand: list):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand[::]
