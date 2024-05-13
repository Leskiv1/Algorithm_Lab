import unittest
from src.minimum_length_of_cable_between_wells import read


class MyTestCase(unittest.TestCase):
    def test_random_vertex(self):
        result = read('../resources/input_files_for_minimum_length_of_cable_between_wells/communication_wells.csv')
        self.assertEqual(result, 37)

        result1 = read(
            '../resources/input_files_for_minimum_length_of_cable_between_wells/another_communication_wells.csv')
        self.assertEqual(result1, 19)

    def test_graph_with_unconnected_wells(self):
        result = read(
            '../resources/input_files_for_minimum_length_of_cable_between_wells/communication_wells_with_unconnected_wells.csv')
        self.assertEqual(result, -1)

    def test_empty_graph(self):
        result = read(
            '../resources/input_files_for_minimum_length_of_cable_between_wells/communication_wells_with_no_vertex.csv')
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
