import unittest


# O(n) time | O(d) space where d is the depth of the tree
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode, min_value=float('-inf'), max_value=float('inf')):
    if root is None:
        return True
    if root.value < min_value or root.value >= max_value:
        return False
    is_left_valid = is_valid_bst(root.left, min_value, root.value)
    is_right_valid = is_valid_bst(root.right, root.value, max_value)
    return is_left_valid and is_right_valid


class TestIsValidBst(unittest.TestCase):
    def test_is_valid_bst(self):
        self.assertEqual(True, is_valid_bst(TreeNode(15, TreeNode(10, None, None), None)))
        self.assertEqual(False, is_valid_bst(TreeNode(10, TreeNode(17, None, None), TreeNode(15, None, None))))
        self.assertEqual(True, is_valid_bst(TreeNode(10, None, None)))


if __name__ == "__main__":
    unittest.main()
