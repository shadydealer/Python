import unittest

from targets import *

class TestWeek01(unittest.TestCase):
    
    #
    # Tests for sum_of_digits(number) function
    #

    def test_sum_of_digits_value(self):
        with self.assertRaises(ValueError):
            sum_of_digits("asd")        
    def test_sum_of_digits_result(self):
        self.assertEqual(sum_of_digits(1234), 10)
    def test_sum_of_digits_for_negative(self):
        self.assertEqual(sum_of_digits(-1234), 10)

    #
    # Tests for to_digits(number) function
    #

    def test_to_digits_value(self):
        with self.assertRaises(ValueError):
            to_digits("asd")
    def test_to_digits_result(self):
        self.assertEqual(to_digits(1234), [1,2,3,4])

    #
    # Tests for the to_nummber(list) function
    #

    def test_to_number_result(self):
        self.assertEqual(to_number([1,2,3,4]), 1234)

    #
    # Tests for fact_digits 
    #

    def test_fact_digits_value(self):
        with self.assertRaises(ValueError):
            fact_digits("asd")

    def test_fact_digits_result(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(999),1088640)

    
    #
    # Tests for nth_fibonacci
    #
    def test_nth_fibonacci_result(self):
        self.assertEqual(nth_fibonacci(10),55)
    

    #
    # Tests for fibonacci as list
    #
    def test_fib_list_value_string(self):
        with self.assertRaises(ValueError):
            fib_list("asd")
    
    def test_fib_list_value_zero(self):
        with self.assertRaises(ValueError):
            fib_list(0)

    def test_fib_list_result(self):
        self.assertEqual(fib_list(5), [1,1,2,3,5])

if __name__ == "__main__":
    unittest.main()