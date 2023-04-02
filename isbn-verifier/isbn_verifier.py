import re


def is_valid(isbn: str):

    isbn = re.sub('[^0-9X]', '', isbn)   # cleanup on isle 2
    isbn_valid_match = re.match('^[0-9]{9}([0-9]|X)$', isbn)
    if not isbn_valid_match:
        return False

    isbn_digits: list[str] = list(isbn)   # Type annotation
    if isbn_digits[-1] == 'X':
        isbn_digits[-1] = 10

    return sum([int(j) * (10 - i) for i, j in enumerate(isbn_digits)]) % 11 == 0
