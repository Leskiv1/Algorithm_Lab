import unittest
from src.number_of_islands_in_matrix import take_element_position_from_matrix, bfs


class Find_Islands(unittest.TestCase):
    def test_random_graph(self):
        self.matrix = [
            [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        ]
        self.assertEqual(take_element_position_from_matrix(self.matrix), 5)

    def test_empty_graph(self):
        self.matrix = []
        self.assertEqual(take_element_position_from_matrix(self.matrix), 0)

    def test_graph_with_all_zero_element(self):
        self.matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(take_element_position_from_matrix(self.matrix), 0)

    def test_graph_with_all_element_is_one(self):
        self.matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(take_element_position_from_matrix(self.matrix), 1)

    def test_bfs(self):
        self.matrix = [
            [1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0]
        ]
        visited = set()
        bfs((3, 4), visited, self.matrix)
        self.assertEqual(len(visited), 8)


if __name__ == '__main__':
    unittest.main()