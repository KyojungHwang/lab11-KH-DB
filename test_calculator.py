# https://github.com/KyojungHwang/lab11-KH-DB
# Partner 1: KyoJung Hwang
# Partner 2: Dennis Bamaca Perez

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    # Dennis will complete:
    # test_add
    # test_subtract
    ########

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

    ######## Partner 2
    # Dennis will complete:
    # test_divide_by_zero
    # test_logarithm
    # test_log_invalid_base
    ########

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
