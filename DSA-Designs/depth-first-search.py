"""All the nodes are also known as vertices
Time complexity - O(V+E) |  Space complexity - O(V)
We are adding a bunch of frames on the call stack for each of the calls on the BFS for each of the vertices(V)
"""
import unittest


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self


def depth_first_search(node, array):
    array.append(node.name)
    for child in node.children:
        child.depth_first_search(array)
    return array


class TestDepthFirstSearch(unittest.TestCase):
    def test_depth_first_search(self):
        node = Node(1)
        node.children = [1, 2, 3, [23, 56, 43, 7, [67, 34, 21, 90]], 67, 89]
        self.assertEqual([], depth_first_search(node, [45]))


if __name__ == "__main__":
    unittest.main()
