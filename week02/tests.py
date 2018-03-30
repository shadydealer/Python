import unittest

from simplify_fraction import *

class TestsFractionSimplification(unittest.TestCase):
    def test_gcd_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            gcd(1,0)
    def test_zero_as_denom(self):
        with self.assertRaises(ZeroDivisionError):
            simplify_fraction((0,0))
    def test_simplification_result(self):
        self.assertEqual(simplify_fraction((1,4)), (1,4))

if __name__ == "__main__":
    unittest.main() 