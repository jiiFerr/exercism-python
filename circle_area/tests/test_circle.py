import unittest 
from math import pi

from circle import circle_area
from circle import raiseValueErrorifInputNeg
from circle import raiseValueErrorifInputNonNumeric

#import circle

class TestCircleArea(unittest.TestCase):

    # Test Area Valid
    def testAreaPostive(self):
        self.assertAlmostEqual(circle_area(2), 12.5663706)

    # Test Radius input valid
    def test_RadiusValid(self):
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 **2)
        self.assertRaises(ValueError, circle_area, -1)  

    def test_raiseValueError(self):
        self.assertRaises(ValueError, raiseValueErrorifInputNeg, -1)

    def test_raiseValueErrorifInputNonNumeric(self):
        self.assertRaises(TypeError, raiseValueErrorifInputNonNumeric, 'j')

    if __name__ == '__main__':
        unittest.main()
