def value(colors):
    return int(str(colour_codes().index(colors[0].lower())) + str(colour_codes().index(colors[1].lower())))


def colour_codes():
    return ["black", "brown", "red",
            "orange", "yellow", "green",
            "blue", "violet", "grey", "white"]

