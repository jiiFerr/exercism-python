"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """

    x = 0
    if card in ['J', 'Q', 'K']:
        x = 10
    elif card == 'A':
        x = 1
    else:
        x = int(card)
    return x


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    :param card_one: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :param card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one: str, card_two: str):
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - card (J, Q, K == 10, numerical value otherwise)
    :param card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    return 11 if value_of_card(card_one) + value_of_card(card_two) < 11 else 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    return bool((value_of_card(card_one) == 1 and value_of_card(card_two) == 10)
                or (value_of_card(card_two) == 1 and value_of_card(card_one) == 10))


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    return bool(value_of_card(card_one) == value_of_card(card_two))


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """

    return bool(9 <= value_of_card(card_one) + value_of_card(card_two) <= 11)
