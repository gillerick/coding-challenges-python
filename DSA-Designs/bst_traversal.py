import unittest

from adt import BST


def in_order_traversal(tree: BST, array: list[int]):
    if tree is not None:
        in_order_traversal(tree.left, array)
        array.append(tree.value)
        in_order_traversal(tree.right, array)
    return array


def pre_order_traversal(tree: BST, array: list[int]):
    if tree is not None:
        array.append(tree.value)
        pre_order_traversal(tree.left, array)
        pre_order_traversal(tree.right, array)
    return array


def post_order_traversal(tree: BST, array: list[int]):
    if tree is not None:
        post_order_traversal(tree.left, array)
        post_order_traversal(tree.right, array)
        array.append(tree.value)
    return array


test_tree = BST(10, left=BST(5, right=BST(5), left=BST(2, left=BST(1), right=None)),
                right=BST(15, left=None, right=BST(22)))


class TestBstTreeTraversal(unittest.TestCase):
    def test_in_order_traversal(self):
        self.assertEqual([1, 2, 5, 5, 10, 15, 22], in_order_traversal(test_tree, []))

    def test_pre_order_traversal(self):
        self.assertEqual([10, 5, 2, 1, 5, 15, 22], pre_order_traversal(test_tree, []))

    def test_post_order_traversal(self):
        self.assertEqual([1, 2, 5, 5, 22, 15, 10], post_order_traversal(test_tree, []))


if __name__ == "__main__":
    unittest.main()
