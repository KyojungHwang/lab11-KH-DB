# https://github.com/KyojungHwang/lab11-KH-DB
# Partner 1: KyoJung Hwang
# Partner 2: Dennis Bamaca Perez

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 3), -1)
        self.assertEqual(add(0, 8), 8)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-4, 3), -7)
        self.assertEqual(sub(8, 0), 8)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 3), -12)
        self.assertEqual(mul(0, 8), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(-2, 10), -5.0)
        self.assertAlmostEqual(div(4, 0), 0.0)
    ########

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(3, 9), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
            
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)

        with self.assertRaises(ValueError):
            square_root(-1)
    ########


# Do not touch this
if __name__ == "__main__":
    unittest.main()
