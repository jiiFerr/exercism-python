def say(number):

    if number < 0 or number > 999_999_999_999: raise ValueError('input out of range')

    saynum = {
        '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three',
        '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven',
        '8' : 'eight', '9' : 'nine', '10': 'ten', '11': 'eleven',
        '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
        '20': 'twenty', '30': 'thirty', '40': 'forty',
        '50': 'fifty', '60': 'sixty', '70': 'seventy',
        '80': 'eighty', '90': 'ninety', '00': 'hundred',
        '000': 'thousand', '000000': 'million', '000000000' : 'billion'
    }

    pos_array = list(reversed(str(number)))

    number_spoken =''
    for posn, value in enumerate(pos_array):
            if posn in [2,3,6,9] and int(value) > 0:
                if len(number_spoken) > 0:
                    number_spoken = saynum.get(value) + ' ' + saynum.get(posn * '0') + ' ' + number_spoken
                else:
                    number_spoken = saynum.get(value) + ' ' + saynum.get(posn * '0')
            elif posn == 0 and len(pos_array) == 1:
                number_spoken = saynum.get(value)
            elif posn == 1:
                if int(value) < 2 and int((pos_array[posn - 1])) > 0:
                    number_spoken = number_spoken + saynum.get(value + pos_array[posn - 1])
                elif int(value) >= 2 and int(pos_array[posn -1]) > 0:
                    number_spoken = number_spoken + saynum.get(value + '0') + "-" + saynum.get(pos_array[posn - 1])
                elif int(pos_array[posn - 1])  == 0 and int(value) > 0:
                    number_spoken = number_spoken + saynum.get(value + '0')

    return number_spoken

