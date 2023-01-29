import unittest

"""
    O(n/2) ~ O(n) time | O(1) space
"""


def move_element_to_the_end(array, to_move):
    left_idx = 0
    right_idx = len(array) - 1
    while left_idx < right_idx:
        left_num = array[left_idx]
        right_num = array[right_idx]
        if left_num == to_move and right_num != to_move:
            # Swap the numbers
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
            left_idx += 1
            right_idx -= 1
        elif right_num == to_move:
            right_idx -= 1
        elif left_num != to_move:
            left_idx += 1
    return array


class TestMoveElementToTheEnd(unittest.TestCase):
    def test_move_element_to_the_end(self):
        self.assertSetEqual({1, 3, 4, 2, 2, 2, 2, 2}, set(move_element_to_the_end([2, 1, 2, 2, 2, 3, 4, 2], 2)))
        self.assertEqual([], move_element_to_the_end([], 6))
        self.assertEqual({3, 3, 3, 3, 3, 3}, set(move_element_to_the_end([3, 3, 3, 3, 3, 3], 3)))
        self.assertEqual({1, 2, 4, 5, 3}, set(move_element_to_the_end([3, 1, 2, 4, 5], 3)))
        self.assertEqual({1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5},
                         set(move_element_to_the_end([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5)))


if __name__ == "__main__":
    unittest.main()
