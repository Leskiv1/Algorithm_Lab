import unittest
from Algorithm_Lab.src.find_usorted_subarray import find_unsort_arr


class MyTestCase(unittest.TestCase):
    def test_one_element(self):
        array = [1]
        self.assertEqual(find_unsort_arr(array), (-1, -1))

    def test_is_sorted(self):
        array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_unsort_arr(array), (-1, -1))

    def test_all_need_sorted(self):
        array = [10, 3, 5, 2, 1]
        self.assertEqual(find_unsort_arr(array), (0, len(array) - 1))
        
    def test_different_array(self):
        array1 = [1, 2, 3, 88, 66, 44, 66, 99, 55, 101, 102, 103, 104, 106, 106]
        array2 = [1, 3, 10, 7, 5, 2, 6, 10, 12, 15]
        self.assertEqual(find_not_sort_range(array1), (3, 8))
        self.assertEqual(find_not_sort_range(array2), (1, 6))


if __name__ == '__main__':
    unittest.main()
