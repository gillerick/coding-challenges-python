import unittest


# O(n) time | O(1) space
def maximum_subarray(nums: list[int]):
    max_sum = nums[0]
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, 0)
    return max_sum


"""
This solution uses a dp array dp of length n where n is the number of elements in the input array nums. The idea 
is to keep track of the maximum subarray sum ending at each index i in the dp array. dp[i] represents the maximum 
subarray sum ending at index i in nums. We start by initializing dp[0] = nums[0], meaning that the maximum subarray 
sum ending at index 0 in nums is simply the first element in the array. 

In each iteration of the loop, we calculate dp[i] as the maximum of either:
(1) the current number nums[i], or
(2) the sum of the current number nums[i] and the maximum subarray sum ending at the previous index dp[i-1]

We update the maximum subarray sum seen so far by keeping track of the maximum value in dp using the max_sum 
variable, and updating it whenever a new maximum value is found. Finally, we return the max_sum variable, 
which represents the maximum subarray sum in nums.

"""


def maximum_subarray_dp(nums: list[int]) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum


class TestMaximumSubArray(unittest.TestCase):
    def test_maximum_subarray(self):
        self.assertEqual(6, maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, maximum_subarray([1]))
        self.assertEqual(23, maximum_subarray([5, 4, -1, 7, 8]))

    def test_maximum_subarray_dp(self):
        self.assertEqual(6, maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, maximum_subarray([1]))
        self.assertEqual(23, maximum_subarray([5, 4, -1, 7, 8]))


if __name__ == "__main__":
    unittest.main()
