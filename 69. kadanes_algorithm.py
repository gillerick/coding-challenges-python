import unittest


def kadanes_algorithm(array):
    maximum_sum = sum(array)
    for i in range(len(array)):
        right_idx = i + 1
        while right_idx <= len(array):
            current_sum = sum(array[i:right_idx])
            maximum_sum = max(maximum_sum, current_sum)
            right_idx += 1
    return maximum_sum


class TestKadanesAlgorithm(unittest.TestCase):
    def test_kadanes_algorithm(self):
        self.assertEqual(19, kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
        self.assertEqual(-1, kadanes_algorithm([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]))
        self.assertEqual(-1, kadanes_algorithm([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
        self.assertEqual(55, kadanes_algorithm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == "__main__":
    unittest.main()
