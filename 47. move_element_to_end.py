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


# O(n) time | O(1) space
def move_element_to_the_end_pivot(array, to_move):
    pivot = 0
    for i in range(len(array)):
        if array[i] != to_move:
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1
    return array


# O(n/2) ~ O(n) time | O(1) space NB: Most efficient
def move_element_to_the_end_two_pointer(array, to_move):
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
        self.assertEqual([1, 3, 4, 2, 2, 2, 2, 2], move_element_to_the_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
        self.assertEqual([], move_element_to_the_end([], 6))
        self.assertEqual([3, 3, 3, 3, 3, 3], move_element_to_the_end([3, 3, 3, 3, 3, 3], 3))
        self.assertEqual([1, 2, 4, 5, 3], move_element_to_the_end([3, 1, 2, 4, 5], 3))

    def test_move_element_to_the_end_two_pointer(self):
        self.assertEqual([], move_element_to_the_end_two_pointer([], 6))
        self.assertEqual({3, 3, 3, 3, 3, 3}, set(move_element_to_the_end_two_pointer([3, 3, 3, 3, 3, 3], 3)))
        self.assertSetEqual({1, 3, 4, 2, 2, 2, 2, 2},
                            set(move_element_to_the_end_two_pointer([2, 1, 2, 2, 2, 3, 4, 2], 2)))
        self.assertEqual({1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5},
                         set(move_element_to_the_end_two_pointer([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12],
                                                                 5)))
        self.assertEqual({1, 2, 4, 5, 3}, set(move_element_to_the_end_two_pointer([3, 1, 2, 4, 5], 3)))

    def test_move_element_to_the_end_pivot(self):
        self.assertEqual([], move_element_to_the_end_pivot([], 6))
        self.assertEqual({3, 3, 3, 3, 3, 3}, set(move_element_to_the_end_pivot([3, 3, 3, 3, 3, 3], 3)))
        self.assertSetEqual({1, 3, 4, 2, 2, 2, 2, 2}, set(move_element_to_the_end_pivot([2, 1, 2, 2, 2, 3, 4, 2], 2)))
        self.assertEqual({1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5},
                         set(move_element_to_the_end_pivot([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5)))
        self.assertEqual({1, 2, 4, 5, 3}, set(move_element_to_the_end_pivot([3, 1, 2, 4, 5], 3)))


if __name__ == "__main__":
    unittest.main()
