import unittest
import csv

from queries import filter
from queries import get_valid_keywords_from_csv
from queries import split_post_and_pre_csv_sifting_commands
from queries import map_keywords
from queries import sift_csv_file

validFileName = "example_data.csv"
validKeywords ={'full_name': 0,
                'favourite_color': 1,
                'company_name': 2,
                'email': 3,
                'phone_number': 4,
                'salary': 5}

class TestQueries(unittest.TestCase):
    
    def test_get_valid_keywords_from_csv_Result(self):
        with open(validFileName) as csvFile:
            self.assertEqual(get_valid_keywords_from_csv(csvFile),validKeywords)

    def test_get_csv_data_raises_OSError_if_fails_to_open_file(self):
        with self.assertRaises(OSError):
            invalidFileName = "qodwqopdkq.csv"
            filter(invalidFileName)
    
    def test_map_keywords_raises_ValueError_if_you_pass_in_a_keyword_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            map_keywords(validKeywords, {'invalid_argument': 'Nope'})
    
    def test_split_post_and_pre_csv_sifting_commands_Result(self):
        mappedKeywords = map_keywords(validKeywords, {'full_name':'Michael Olson'})
        self.assertEqual(split_post_and_pre_csv_sifting_commands(mappedKeywords),
                         [{}, {'Michael Olson' : 0}])

    def test_map_keywords_on_an_existing_keyword(self):
            self.assertEqual(map_keywords(validKeywords, {'salary' : 'Yep'}),{'Yep' : 5})

    def test_sift_csv_file_Result(self):
        with open(validFileName) as csvFile:
            validOutputList = [['Michael Olson',
                                'olive',
                                'Scott, Young and King',
                                'zacharymcdonald@yahoo.com',
                                '114-116-1124x315',
                                '2151']]
            self.assertEqual(sift_csv_file(csvFile,{'Michael Olson' : [0]}),
                             validOutputList)

if __name__ == '__main__':
    unittest.main()
