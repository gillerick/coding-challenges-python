import unittest


def binary_search(array, target):
    left_idx = 0
    right_idx = len(array) - 1
    while left_idx <= right_idx:
        mid = (left_idx + right_idx) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right_idx = mid - 1
        elif array[mid] < target:
            left_idx = mid + 1

    return -1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(3, binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
        self.assertEqual(3, binary_search([1, 5, 23, 111], 111))
        self.assertEqual(1, binary_search([1, 5, 23, 111], 5))
        self.assertEqual(-1, binary_search([1, 5, 23, 111], 35))
        self.assertEqual(0, binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))


if __name__ == "__main__":
    unittest.main()
