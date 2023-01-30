"""
Recursive solution:
"""
import unittest


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode, lower=float('-inf'), upper=float('inf')):
    if not root:
        return True
    if not lower < root.value < upper:
        return False
    return is_valid_bst(root.left, lower, root.value) and is_valid_bst(root.right, root.value, upper)


class TestIsValidBst(unittest.TestCase):
    def test_is_valid_bst(self):
        self.assertEqual(True, is_valid_bst(TreeNode(15, TreeNode(10, None, None), None)))
        self.assertEqual(True, is_valid_bst(TreeNode(10, None, None)))
        self.assertEqual(False, is_valid_bst(TreeNode(10, TreeNode(17, None, None), TreeNode(15, None, None))))


if __name__ == "__main__":
    unittest.main()
