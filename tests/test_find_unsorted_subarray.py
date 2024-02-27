import unittest
from degree_3 import find_min_max_elements


class MyTestCase(unittest.TestCase):
    def test_one_element(self):
        array = [1]
        min_index, max_index = find_min_max_elements(array)
        self.assertEqual(min_index, -1)
        self.assertEqual(max_index, -1)

    def test_is_sorted(self):
        array = [1, 2, 3, 4, 5, 6]
        min_index, max_index = find_min_max_elements(array)
        self.assertEqual(min_index, -1)
        self.assertEqual(max_index, -1)

    def test_all_need_sorted(self):
        array = [10, 3, 5, 2, 1]
        min_index, max_index = find_min_max_elements(array)
        self.assertEqual(min_index, 0)
        self.assertEqual(max_index, len(array) - 1)


if __name__ == '__main__':
    unittest.main()
