import re


def response(hey_bob: str):
    """
    Reply generator, from conditional string parsing, and pattern matching.:w

    :param hey_bob:
    :return: str - Bob's mumbled, indifferent, teenage response.
    """
    resp_txt = ''

    """
    NOTES:
        'match' tries to match from the beginning of the line..
         re.DOTALL - Makes '.' include \n. It doesn't by default.
    """
    if not isinstance(hey_bob, str):
        raise ValueError("Bob needs a sentence.")

    if re.findall('[?]', hey_bob, re.MULTILINE):
        # best so far - if re.search("\b([A-Z' !])+\b\?", hey_bob):
        if re.search("[A-Z]+\?", hey_bob):
            resp_txt = 'Calm down, I know what I\'m doing!'
        # safe - elif re.search('(?<=\?).+', hey_bob, re.DOTALL):
        elif re.search('(?<=\?)(\n)?\S+$', hey_bob, re.MULTILINE):
            resp_txt = 'Whatever.'
        else:
            resp_txt = 'Sure.'

    # most stable - elif re.search('[A-Z0-9]+[!]?$', hey_bob, re.DOTALL):
    elif re.search('[A-Z]+[0-9]*[!]?$', hey_bob, re.DOTALL):
    # elif re.search('\w+[!]?$', hey_bob, re.DOTALL):
        resp_txt = 'Whoa, chill out!'
    elif re.match('^([ ]+|\t+)?$', hey_bob, re.M):
        resp_txt = 'Fine. Be that way!'
    else:
        resp_txt = 'Whatever.'

    return resp_txt
