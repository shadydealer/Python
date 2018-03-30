import unittest

from money_tracker import extract_date

class MoneyTrackerTests(unittest.TestCase):
    def test_extract_date_value(self):
        with self.assertRaises(ValueError):
            extract_date("=== 12.03-2012 ===")
    def test_extract_date_result(self):
            self.assertEquals(extract_date("=== 12-03-2018 ==="), 2018312);
    #checks whether the date is valid.
    def test_show_user_by_date_Value(self):
        with self.assertRaises(ValueError):
            show_user_data_by_date("a2-03-2018")
            show_user_data_by_date("01-01-2019")

    def test_show_user_data_by_date_result(self):
        assertEquals(show_user_data_by_date("22-03-2018"),);


if __name__ == "__main__":
    unittest().main()