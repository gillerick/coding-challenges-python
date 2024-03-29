import unittest


# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence
# by removing no more than one element from the array. Note: sequence a0, a1, ..., an is considered to be a strictly
# increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

def almost_increasing_sequence(arr: list[int]):
    count = 0
    increasing = False
    for i in range(len(arr)):
        temp_array = arr.copy()
        temp_array.remove(arr[i])
        count = 0
        for j in range(1, len(temp_array)):
            if temp_array[j - 1] < temp_array[j]:
                increasing = True
            else:
                count += 1
    return True if increasing and count == 0 else False


# ToDO: Fix failing tests
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
