class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_tree_balanced(node: BinaryTree):
    balanced = True

    def depth_first_search(node):
        if not node:
            return 0

        left_under_tree = depth_first_search(node.left)
        right_under_tree = depth_first_search(node.right)

        if abs(left_under_tree - right_under_tree) > 1:
            nonlocal balanced
            balanced = False

        return 1 + max(left_under_tree, right_under_tree)

    depth_first_search(node)

    return balanced



