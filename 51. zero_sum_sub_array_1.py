import unittest


# O(n) time | O(n) space
def zero_sum_subarray(nums):
    sums = {0}
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in sums:
            return True
        sums.add(current_sum)
    return False


class TestZeroSumSubArray(unittest.TestCase):
    def test_zero_sum_subarray(self):
        self.assertEqual(True, zero_sum_subarray([1, 2, -2, 3]))
        self.assertEqual(True, zero_sum_subarray([0, 0, 0]))
        self.assertEqual(False, zero_sum_subarray([9]))
        self.assertEqual(True, zero_sum_subarray([1, 2, 3, 4, 0, 5, 6, 7]))
        self.assertEqual(False, zero_sum_subarray([1, 2, 3]))
        self.assertEqual(True, zero_sum_subarray([2, -2]))
        self.assertEqual(False, zero_sum_subarray([1, 1, 1]))
        self.assertEqual(True, zero_sum_subarray([-1, 2, 3, 4, -5, -3, 1, 2]))
        self.assertEqual(False, zero_sum_subarray([-1, -1, -1]))


if __name__ == "__main__":
    unittest.main()
