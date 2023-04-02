def commands(binary_str: str):
    secret_handshake = []

    hands = {
        "1": "wink",
        "10": "double blink",
        "100": "close your eyes",
        "1000": "jump",
        # "10000": reverse
    }

    for ctr, binary_char in enumerate(reversed(list(binary_str))):

        if binary_char == '1':
            if ctr == 4:
                secret_handshake = secret_handshake[::-1]
            elif 0 < ctr < 4:
                secret_handshake.append(hands.get(binary_char + str('0' * ctr)))
            else:
                secret_handshake.append(hands.get(binary_char))

    return secret_handshake
