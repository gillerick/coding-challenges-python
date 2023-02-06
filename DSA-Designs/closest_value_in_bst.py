import unittest


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def closest_value_in_bst(root: BST, target: int, closest=float("inf")):
    if root is None:
        return closest

    if abs(target - root.value) < abs(target - closest):
        closest = root.value

    if target > root.value:
        return closest_value_in_bst(root.right, target, closest)
    elif target < root.value:
        return closest_value_in_bst(root.left, target, closest)
    else:
        return closest


class TestClosesValueInBst(unittest.TestCase):
    def test_closest_value_in_bst(self):
        tree = BST(10, left=BST(5, right=BST(5), left=BST(2, BST(1))),
                   right=BST(15, left=BST(13, right=BST(14)), right=BST(22)))
        self.assertEqual(13, closest_value_in_bst(tree, 12))


if __name__ == "__main__":
    unittest.main()
