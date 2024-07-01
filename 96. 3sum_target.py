import unittest


def three_sum_target(nums, target):
    nums.sort()
    three_sum_array = []
    seen_triplets = set()

    for i in range(len(nums) - 2):
        left_index = i + 1
        right_index = len(nums) - 1
        while left_index < right_index:
            current = nums[i]
            left = nums[left_index]
            right = nums[right_index]
            current_sum = current + left + right
            if current_sum == target:
                triplet = tuple([current, left, right])
                if triplet not in seen_triplets:
                    three_sum_array.append([current, left, right])
                    seen_triplets.add(triplet)
                left_index += 1
                right_index -= 1
            elif current_sum < target:
                left_index += 1
            elif current_sum > target:
                right_index -= 1

    return three_sum_array


class TestThreeSum(unittest.TestCase):
    def test_three_sum_zero_target(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], three_sum_target([-1, 0, 1, 2, -1, -4], 0))
        self.assertEqual([], three_sum_target([0, 1, 1], 0))
        self.assertEqual([[0, 0, 0]], three_sum_target([0, 0, 0], 0))

    def test_no_triplets(self):
        self.assertEqual([[1, 4, 5], [2, 3, 5]], three_sum_target([1, 2, 3, 4, 5], 10))
        self.assertEqual([[-5, -4, -1], [-5, -3, -2]], three_sum_target([-1, -2, -3, -4, -5], -10), )

    def test_multiple_triplets(self):
        self.assertEqual([[-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1]], three_sum_target([1, 2, -2, -1, 0, 1, -1, 1], 0))
        self.assertEqual([[-4, 2, 4], [-1, -1, 4], [-1, 0, 3], [-1, 1, 2]], three_sum_target([4, -1, -1, 0, 1, 2, -4, 3], 2))

    def test_single_element_array(self):
        self.assertEqual(three_sum_target([1], 1), [])
        self.assertEqual(three_sum_target([-1], -1), [])

    def test_two_element_array(self):
        self.assertEqual(three_sum_target([1, 2], 3), [])
        self.assertEqual(three_sum_target([-1, -2], -3), [])

    def test_empty_array(self):
        self.assertEqual(three_sum_target([], 0), [])


if __name__ == "__main__":
    unittest.main()
