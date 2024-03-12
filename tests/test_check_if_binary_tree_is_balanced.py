import unittest
from src.check_if_binary_tree_is_balanced import is_tree_balanced, BinaryTree


class TestBinaryTree(unittest.TestCase):
    def test_balanced_tree1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        self.assertTrue(is_tree_balanced(root))

    def test_balanced_tree2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.right.right.right = BinaryTree(9)

        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(5)

        self.assertFalse(is_tree_balanced(root))

    def test_unbalanced_tree2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.right.right = BinaryTree(5)
        root.left.left.left = BinaryTree(6)
        root.right.right.right = BinaryTree(7)

        self.assertFalse(is_tree_balanced(root))

    def test_one_element_tree(self):
        root = BinaryTree(1)

        self.assertTrue(is_tree_balanced(root))


if __name__ == '__main__':
    unittest.main()
