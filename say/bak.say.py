def say(number):
    number_spoken = ''

    saynum = {
        '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three',
        '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven',
        '8' : 'eight', '9' : 'nine', '10': 'ten', '11': 'eleven',
        '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen',
        '20': 'twenty', '30': 'thirty', '40': 'forty',
        '50': 'fifty', '60': 'sixty', '70': 'seventy',
        '80': 'eighty', '90': 'ninety', '00': 'hundred',
        '000': 'thousand', '000,000': 'million', '000,000,000' : 'billion'
    }

    pos_array = list(reversed(str(number)))

    for posn, value in enumerate(pos_array):
        #if value > 0:
        if posn == 9:
            number_spoken = saynum.get(value) + ' ' + saynum.get('000,000,000')
        elif posn == 6:
	        number_spoken = saynum.get(value) + ' ' + saynum.get('000,000')
        # elif posn == 5:
        #     number_spoken = saynum.get(value) + ' ' + saynum.get('000,000')
        elif posn == 3:
            # number_spoken = number_spoken + ' ' + saynum.get(value) + ' ' + saynum.get('000')
            number_spoken = saynum.get(value) + ' ' + saynum.get('000')
        elif posn == 2:
            number_spoken = saynum.get(value) + ' ' + saynum.get('00')
        elif posn == 0 and len(pos_array) == 1:
            number_spoken = saynum.get(value)
        elif posn == 1:
            if int(value) < 2 and int((pos_array[posn - 1])) > 0:
                number_spoken = number_spoken + saynum.get(value + pos_array[posn - 1])
            elif int(value) >= 2 and int(pos_array[posn -1]) > 0:
                number_spoken = number_spoken + saynum.get(value + '0') + "-" + saynum.get(pos_array[posn - 1])
            elif int(pos_array[posn - 1]) == 0:
                number_spoken = number_spoken + saynum.get(value + '0')

	        # else:
	        #     number_spoken = saynum.get(value)

    return number_spoken

