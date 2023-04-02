from typing import List, Any


def slices(series, length):

    if len(series) == 0 or length < 1:
        raise ValueError("input series string must not be empty; slice length must be non-zero")

    if len(series) < length:
        exception_string = "Substring length {} cannot be Greater than " \
                           "the length of the input string {}, {}".format(length, series, len(series) )
        raise ValueError(exception_string)


    # "List comprehensions"
    return [series[i:i+length] for i in range(len(series) - length + 1)]
