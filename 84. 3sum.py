import unittest


def three_sum(nums):
    nums.sort()
    three_sums = []
    seen = set()
    for i in range(len(nums) - 2):
        left_idx = i + 1
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            left = nums[left_idx]
            right = nums[right_idx]
            current = nums[i]
            current_sum = current + left + right
            if current_sum == 0:
                triplet = tuple([current, left, right])
                if triplet not in seen:
                    three_sums.append([current, left, right])
                    seen.add(triplet)
                right_idx -= 1
                left_idx += 1
            elif current_sum > 0:
                right_idx -= 1
            elif current_sum < 0:
                left_idx += 1
    return three_sums


class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([], three_sum([0, 1, 1]))
        self.assertEqual([[0, 0, 0]], three_sum([0, 0, 0]))


if __name__ == "__main__":
    unittest.main()
