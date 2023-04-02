

def response(hey_bob: str):
    """
    Reply generator, from conditional string parsing

    :param hey_bob:
    :return: str - Bob's mumbled, indifferent, teenage response.
    """
    if not isinstance(hey_bob, str):
        raise ValueError("Bob needs a sentence.")

    say_bob = hey_bob.strip()
    bob_says = ''

    if not say_bob:
        bob_says = 'Fine. Be that way!'
    elif say_bob.isupper() and say_bob.endswith('?'):
        bob_says = 'Calm down, I know what I\'m doing!'
    elif say_bob.isupper():
        bob_says = 'Whoa, chill out!'
    elif say_bob.endswith('?'):
        bob_says = 'Sure.'
    else:
        bob_says = 'Whatever.'

    return bob_says
