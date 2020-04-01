def is_armstrong_number(number):
    input_number = str(number)
    base = len(input_number)
    result = 0

    digit_list = [input_number[i:i + 1] for i in range(0, base, 1)]
    for digit in digit_list:
        result += int(digit)**base

    return True if result == number else False
