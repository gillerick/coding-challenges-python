import unittest

from adt import BST


def maximum_depth_of_binary_tree_recursive(root: BST):
    def dfs(node: BST, depth):
        if node is None:
            return depth
        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

    return dfs(root, 0)


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_maximum_depth_of_binary_tree_recursive(self):
        self.assertEqual(1, maximum_depth_of_binary_tree_recursive(BST(None)))
        self.assertEqual(3, maximum_depth_of_binary_tree_recursive(BST(None, BST(1, BST(2)))))
        self.assertEqual(2, maximum_depth_of_binary_tree_recursive(BST(None, BST(1, None))))


if __name__ == "__main__":
    unittest.main()
