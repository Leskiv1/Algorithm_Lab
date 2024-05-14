import unittest
from src.find_the_max_possible_wire_length import read


class MyTestCase(unittest.TestCase):
    def test_random_value(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/random_value.csv')
        self.assertEqual(result, 8.94)

        result1 = read('../resources/input_files_for_find_the_max_possible_wire_length/another_random_value.csv')
        self.assertEqual(result1, 396.32)

    def test_all_pillars_have_height_one(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/all_pillars_have_height_one.csv')
        self.assertEqual(result, 300)

    def test_pill_have_height_zero(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/any_pill_have_height_zero.csv')
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
