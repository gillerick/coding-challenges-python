import unittest

"""
    This solution is in-place, it solves the problem without moving the elements into another array
    O(n+m*count) time |
"""


def move_element_to_the_end(array, to_move):
    count = array.count(to_move)
    array = list(filter(lambda x: x != to_move, array))
    array.extend([to_move] * count)
    return array


class TestMoveElementToTheEnd(unittest.TestCase):
    def test_move_element_to_the_end(self):
        self.assertEqual([1, 3, 4, 2, 2, 2, 2, 2], move_element_to_the_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
        self.assertEqual([], move_element_to_the_end([], 6))
        self.assertEqual([3, 3, 3, 3, 3, 3], move_element_to_the_end([3, 3, 3, 3, 3, 3], 3))
        self.assertEqual([1, 2, 4, 5, 3], move_element_to_the_end([3, 1, 2, 4, 5], 3))


if __name__ == "__main__":
    unittest.main()
