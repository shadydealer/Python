import unittest
import csv

from queries import filter
from queries import get_valid_row_filters_from_csv
from queries import split_filters
from queries import map_row_filters
from queries import extract_subarray_by_row_filters

validFileName = "example_data.csv"
validFilters ={'full_name': 0,
                'favourite_color': 1,
                'company_name': 2,
                'email': 3,
                'phone_number': 4,
                'salary': 5}

class TestQueries(unittest.TestCase):
    
    def test_get_valid_row_filters_from_csv_Result(self):
        with open(validFileName) as csvFile:
            self.assertEqual(get_valid_row_filters_from_csv(csvFile),validFilters)

    def test_get_csv_data_raises_OSError_if_fails_to_open_file(self):
        with self.assertRaises(OSError):
            invalidFileName = "qodwqopdkq.csv"
            filter(invalidFileName)
    
    def test_split_filters_Result(self):
        self.assertEqual(split_filters(validFilters,{'full_name':'Michael Olson'}),
                         [{'full_name' : 'Michael Olson'},{}])

    def test_map_row_filters_raises_ValueError_if_you_pass_in_a_filter_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            map_row_filters(validFilters, {'invalid_argument': 'Nope'})

    def test_map_row_filters_on_an_existing_filter(self):
            self.assertEqual(map_row_filters(validFilters, {'salary' : 'Yep'}),{5:'Yep'})

    def test_extract_subarray_by_row_filters_Result(self):
        with open(validFileName) as csvFile:
            validOutputList = [['Michael Olson',
                                'olive',
                                'Scott, Young and King',
                                'zacharymcdonald@yahoo.com',
                                '114-116-1124x315',
                                '2151']]
            self.assertEqual(extract_subarray_by_row_filters(csvFile,{0: 'Michael Olson'}),
                             validOutputList)

if __name__ == '__main__':
    unittest.main()
