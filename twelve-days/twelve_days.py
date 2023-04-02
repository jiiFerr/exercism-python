def recite(start_verse, end_verse):
    carol = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
             ]
    oh_my_days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    all_lines = []
    for verse_count in range(start_verse-1, end_verse, 1):

        lead_line = ["On the " + oh_my_days[verse_count] + " day of Christmas my true love gave to me: "]

        if verse_count > 0:
            verse_lines = ["and " + carol[0]] + carol[1:verse_count+1]
        else:
            verse_lines = carol[:verse_count+1]

        out_string = ""
        out_by = lead_line + verse_lines[::-1]
        for x, y in enumerate(out_by):
            if x == 0:
                out_string = out_string + str(y)
            else:
                out_string = out_string + str(y) + ", "

        all_lines += [out_string.rstrip(', ')]
    return all_lines
