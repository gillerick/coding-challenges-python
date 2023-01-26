import unittest


# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence
# by removing no more than one element from the array. Note: sequence a0, a1, ..., an is considered to be a strictly
# increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

def almost_increasing_sequence(arr: list[int]):
    f1 = sum([1 for a, b in zip(arr[:-1], arr[1:]) if a >= b]) <= 1
    f2 = sum([1 for a, c in zip(arr[:-2], arr[2:]) if a >= c]) <= 1
    return f1 and f2


class TestAlmostIncreasing(unittest.TestCase):
    def test_almost_increasing_arr(self):
        self.assertEqual(True, almost_increasing_sequence([1, 3, 2]))
        self.assertEqual(False, almost_increasing_sequence([1, 3, 2, 1]))
        self.assertEqual(False, almost_increasing_sequence([1, 2, 1, 2]))
        self.assertEqual(False, almost_increasing_sequence([1, 1, 2, 3, 4, 4]))
        self.assertEqual(True, almost_increasing_sequence([1, 2, 3, 4, 3, 6]))


# 12/19 test cases pass

if __name__ == "__main__":
    unittest.main()
