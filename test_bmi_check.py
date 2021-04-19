import unittest

from bmi_check import BMICheck

class TestBmiCheck(unittest.TestCase):

    def test_calculate_bmi(self):
     assert BMICheck().calculate_bmi(1.81,76) == 23

    def test_bmi_category(self):
     assert BMICheck().bmi_category(23) == 'Great shape!'

if __name__ == '__main__':
    unittest.main()
