import unittest
from src.least_numb_of_beer_at_corporate import create_preference_matrix


class Least_Numb_Of_Beer(unittest.TestCase):
    def test_random_value(self):
        self.assertEqual(create_preference_matrix(2, 2, 'YN NY'), 2)
        self.assertEqual(create_preference_matrix(6, 3, 'YNN YNY YNY NYY NYY NYN'), 2)

    def test_the_all_same_preferences(self):
        self.assertEqual(create_preference_matrix(6, 3, 'YNN YNN YNN YNN YNN YNN'), 1)

    def test_one_preference_is_same(self):
        self.assertEqual(create_preference_matrix(8, 5, 'NNNNY NNYNY NYNNY NNNYY YNNYY YNYNY YNNNY YYNNY'), 1)

    def test_no_one_preference_is_same(self):
        self.assertEqual(create_preference_matrix(4, 4, 'YNNN NYNN NNYN NNNY'), 4)

    def test_nobody_likes_beer(self):
        self.assertEqual(create_preference_matrix(4, 3, 'NNN NNN NNN NNN'), 0)


if __name__ == '__main__':
    unittest.main()
