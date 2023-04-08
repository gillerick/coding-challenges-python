import unittest
from collections import deque

from adt import BST


def maximum_depth_of_binary_tree_recursive(root: BST):
    def dfs(node: BST, depth):
        if node is None:
            return depth
        return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))

    return dfs(root, 0)


def maximum_depth_of_binary_tree_bfs(root: BST) -> int:
    if not root:
        return 0
    else:
        level = 0
        queues = deque([root])
        while queues:
            for i in range(len(queues)):
                lefted = queues.popleft()
                if lefted.left:
                    queues.append(lefted.left)
                if lefted.right:
                    queues.append(lefted.right)
            level += 1
        return level


class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def test_maximum_depth_of_binary_tree_recursive(self):
        self.assertEqual(1, maximum_depth_of_binary_tree_recursive(BST(None)))
        self.assertEqual(3, maximum_depth_of_binary_tree_recursive(BST(None, BST(1, BST(2)))))
        self.assertEqual(2, maximum_depth_of_binary_tree_recursive(BST(None, BST(1, None))))

    def test_maximum_depth_of_binary_tree_bfs(self):
        self.assertEqual(1, maximum_depth_of_binary_tree_bfs(BST(None)))
        self.assertEqual(3, maximum_depth_of_binary_tree_bfs(BST(None, BST(1, BST(2)))))
        self.assertEqual(2, maximum_depth_of_binary_tree_bfs(BST(None, BST(1, None))))


if __name__ == "__main__":
    unittest.main()
