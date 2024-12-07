import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):
    # Tests for the power function
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    # Tests for the divide function
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_zero_denominator(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_negative_values(self):
        self.assertEqual(divide(-10, 2), -5)

if __name__ == "__main__":
    unittest.main()
