import unittest

from adt import BST


def minimum_depth_of_binary_tree(root: BST):
    # Base case...
    # If the subtree is empty i.e. root is NULL, return depth as 0...
    if root is None:
        return 0
    # Initialize the depth of two subtrees...
    leftDepth = minimum_depth_of_binary_tree(root.left)
    rightDepth = minimum_depth_of_binary_tree(root.right)
    # If the both subtrees are empty...
    if root.left is None and root.right is None:
        return 1
    # If the left subtree is empty, return the depth of right subtree after adding 1 to it...
    if root.left is None:
        return 1 + rightDepth
    # If the right subtree is empty, return the depth of left subtree after adding 1 to it...
    if root.right is None:
        return 1 + leftDepth
    # When the two child function return its depth...
    # Pick the minimum out of these two subtrees and return this value after adding 1 to it...
    return min(leftDepth, rightDepth) + 1;  # Adding 1 is the current node which is the parent of the two subtrees...


class TestMinimumDepthOfBinaryTree(unittest.TestCase):
    def test_minimum_depth_of_binary_tree(self):
        self.assertEqual(1, minimum_depth_of_binary_tree(BST(None)))


if __name__ == "__main__":
    unittest.main()
