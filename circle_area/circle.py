from math import pi

def circle_area( r ) :

    raiseValueErrorifInputNeg(r)

    area = pi * r**2
    return area

def validateInput(radialInput):
    raiseValueErrorifInputNonNumeric(radialInput)
    raiseValueErrorifInputNeg(radialInput)

def raiseValueErrorifInputNeg(radialInput):
    if radialInput < 0:
        raise ValueError("Input Value Cannot be Negative")

def raiseValueErrorifInputNonNumeric(radialInput):
    if type(radialInput) not in [int, float]:
        raise TypeError("An Int or A Double Value, please.")