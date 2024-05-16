import unittest
from src.find_the_max_possible_wire_length import read


class MyTestCase(unittest.TestCase):
    def test_random_value(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/height_with_value_3.csv')
        self.assertEqual(5.66, result)

        result1 = read(
            '../resources/input_files_for_find_the_max_possible_wire_length/heights_with_value_100_and_2.csv')
        self.assertEqual(396.32, result1)

        result2 = read('../resources/input_files_for_find_the_max_possible_wire_length/heights_with_random_value.csv')
        self.assertEqual(2738.18, result2)

    def test_all_pillars_have_height_one(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/all_pillars_have_height_one.csv')
        self.assertEqual(300, result)

    def test_pill_have_height_zero(self):
        result = read('../resources/input_files_for_find_the_max_possible_wire_length/any_pill_have_height_zero.csv')
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
