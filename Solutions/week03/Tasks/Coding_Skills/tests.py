import unittest

from coding_skills import extract_best_by_skill

json_file_without_people = "peopleless.json"
json_file_without_skills = "skilless.json"

valid_json_file = "data.json"
invalid_json_file_path = "invalid_path.json"

empty_json_file = "empty.json"

class CodingSkillsTests(unittest.TestCase):

    def test_file_is_open(self):
        with self.assertRaises(OSError):
            extract_best_by_skill(invalid_json_file_path)
    
    def test_file_has_people_object(self):
        with self.assertRaises(ValueError):
            extract_best_by_skill(json_file_without_people)

    def test_file_people_objs_have_skill_member(self):
        with self.assertRaises(ValueError):
            extract_best_by_skill(json_file_without_skills)
    def test_extract_best_by_skill_returns_empty_dict(self):
        self.assertEqual(extract_best_by_skill(empty_json_file), {})

if __name__ == '__main__':
        unittest.main()
