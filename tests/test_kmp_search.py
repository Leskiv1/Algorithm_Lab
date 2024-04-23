import unittest
from src.kmp_search import find_longest_prefix_suffix


class MyTestCase(unittest.TestCase):
    def test_random_value(self):
        self.assertEqual(find_longest_prefix_suffix("aaabaaabaaacdaabacd", "aab"), [1, 5, 13])
        self.assertEqual(find_longest_prefix_suffix("abcbaabcdabdcaacd", "abcd"), [5])
        self.assertEqual(find_longest_prefix_suffix("ла ла ла лоло", "ла ло"), [6])

    def test_all_letters_is_same(self):
        self.assertEqual(find_longest_prefix_suffix("aaaa", "a"), [0, 1, 2, 3])

    def test_no_search_word(self):
        self.assertEqual(find_longest_prefix_suffix("aaabaaabaaacdaabacd", "лд"), None)


if __name__ == '__main__':
    unittest.main()
