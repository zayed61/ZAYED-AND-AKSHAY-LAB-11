# https://github.com/zayed61/ZAYED-AND-AKSHAY-LAB-11
# Partner 1: Zayed AlGhfeli
# Partner 2: Akshay Bekkary
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -5), 3)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-3, 2), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(2, -6), -3)
        self.assertAlmostEqual(div(-1, -12), 12)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # According to your calculator.py, div(a, b) raises ZeroDivisionError if a == 0
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        # log(a, b) returns math.log(b, a)
        self.assertAlmostEqual(logarithm(10, 100), 2)      # log base 10 of 100 = 2
        self.assertAlmostEqual(logarithm(2, 8), 3)         # log base 2 of 8 = 3
        self.assertAlmostEqual(logarithm(3, 9), 2)         # log base 3 of 9 = 2

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(10, -3)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 2 ** (1/2))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
