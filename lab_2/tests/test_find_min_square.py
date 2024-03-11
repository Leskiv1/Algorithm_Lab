import unittest
from lab_2.src.find_min_square import least_square


class MyTestCase(unittest.TestCase):
    def test_different_values(self):
        self.assertEqual(least_square(10, 2, 3), 9)
        self.assertEqual(least_square(2, 1000000000, 999999999), None)
        self.assertEqual(least_square(4, 1, 1), 2)

    def test_values_equal_zero(self):
        self.assertEqual(least_square(0, 2, 3), None)
        self.assertEqual(least_square(2, 0, 20), None)
        self.assertEqual(least_square(4, 1, 0), None)


if __name__ == '__main__':
    unittest.main()
