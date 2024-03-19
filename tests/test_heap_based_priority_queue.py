import unittest
from src.heap_based_priority_queue import insert_node, delete_max_priority,  Node


class TestPriorityQueue(unittest.TestCase):
    def our_nodes(self):
        self.arr = []
        self.key1 = Node('11', 11)
        self.key2 = Node('6', 6)
        self.key3 = Node('15', 15)
        self.key4 = Node('9', 9)
        insert_node(self.arr, self.key1)
        insert_node(self.arr, self.key2)
        insert_node(self.arr, self.key3)
        insert_node(self.arr, self.key4)

    def test_insert_node(self,):
        self.our_nodes()
        self.assertEqual(self.key3.priority, self.arr[0].priority)

    def test_delete_max_priority(self):
        self.our_nodes()
        delete_max_priority(self.arr)
        self.assertEqual(self.arr[0].priority, self.key1.priority)

    def our_nodes_all_same(self):
        self.arr = []
        self.key1 = Node('11', 11)
        self.key2 = Node('11', 11)
        self.key3 = Node('11', 11)
        self.key4 = Node('11', 11)
        insert_node(self.arr, self.key1)
        insert_node(self.arr, self.key2)
        insert_node(self.arr, self.key3)
        insert_node(self.arr, self.key4)

    def test_insert_all_same_node(self,):
        self.our_nodes_all_same()
        self.assertEqual(self.key1.priority, self.arr[0].priority)

    def test_delete_max_priority_all_same_node(self):
        self.our_nodes_all_same()
        delete_max_priority(self.arr)
        self.assertEqual(self.arr[0].priority, self.key2.priority)

    def test_there_are_no_nodes(self):
        self.arr = []
        result = delete_max_priority(self.arr)
        self.assertEqual(result, 0)














if __name__ == '__main__':
    unittest.main()
