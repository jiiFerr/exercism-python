saynum = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven',
    '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
    '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
    '20': 'twenty', '30': 'thirty', '40': 'forty',
    '50': 'fifty', '60': 'sixty', '70': 'seventy',
    '80': 'eighty', '90': 'ninety', '00': 'hundred',
    '000': 'thousand', '000000': 'million', '000000000': 'billion'
}

def say(number):

    if number < 0 or number > 999_999_999_999: raise ValueError('input out of range')

    pos_array = list(reversed(str(number)))

    number_spoken =''
    for posn, value in enumerate(pos_array):
        if posn in [0,2,3,6,9]:
            number_spoken = hundred_chunks(posn, pos_array)
            # number_spoken = number_spoken + ' '

    return number_spoken

def hundred_chunks(posn:int, pos_array:list) -> str:
    number_spoken = ''
    chunk_len = 0

    if (posn + 2) <= len(pos_array):
        chunk_len = posn + 2
    else:
        chunk_len =  len(pos_array)

    for i,v in enumerate(pos_array[posn:chunk_len]):
        if i == 2:
            if int(v) > 0:
                number_spoken = saynum.get(v) + ' ' + saynum.get(i * '0')
        elif i == 1:
            if int(v) > 0:
                if int(v) >= 2:
                    number_spoken = number_spoken + saynum.get(v + '0')
                    if int(pos_array[i-1]) > 0:
                        number_spoken = number_spoken + "-" + saynum.get(pos_array[i - 1])
                else:
                    number_spoken = saynum.get(v + pos_array[i - 1])
                break
        elif i == 0:
            if (posn > 0 and int(v) > 0) and (len(pos_array) > 0):
                number_spoken = saynum.get(v)

    if posn > 1:
        number_spoken = number_spoken + saynum.get(posn)

    return number_spoken