import unittest


def zero_sum_subarray(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if sum(nums[i:j + 1]) == 0:
                return True
    return False


class TestZeroSumSubArray(unittest.TestCase):
    def test_zero_sum_subarray(self):
        self.assertEqual(True, zero_sum_subarray([0, 0, 0]))
        self.assertEqual(True, zero_sum_subarray([1, 2, -2, 3]))
        self.assertEqual(False, zero_sum_subarray([9]))
        self.assertEqual(False, zero_sum_subarray([1, 2, 3]))
        self.assertEqual(False, zero_sum_subarray([1, 1, 1]))
        self.assertEqual(True, zero_sum_subarray([2, -2]))
        self.assertEqual(True, zero_sum_subarray([-1, 2, 3, 4, -5, -3, 1, 2]))
        self.assertEqual(False, zero_sum_subarray([-1, -1, -1]))


if __name__ == "__main__":
    unittest.main()
