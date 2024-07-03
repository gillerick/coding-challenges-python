import unittest


# O(n log(n)) - time complexity
def second_smallest(nums):
    if len(nums) == 1:
        return None

    return sorted(nums)[1]


# O(n) - time complexity
def second_smallest_optimized(nums):
    if len(nums) == 1:
        return None

    smallest = float('inf')
    second_smallest_num = float('inf')
    for num in nums:
        if num < smallest:
            second_smallest_num = smallest
            smallest = num
        elif num < second_smallest_num:
            second_smallest_num = num

    return second_smallest_num


class SecondSmallest(unittest.TestCase):
    def test_second_smallest(self):
        self.assertEqual(3, second_smallest([8, 9, 2, 3]))

    def test_second_smallest_optimized(self):
        self.assertEqual(3, second_smallest_optimized([8, 9, 2, 3]))

    def test_second_smallest_less_than_two_items(self):
        self.assertEqual(None, second_smallest([9]))

    def test_second_smallest_optimized_less_than_two_items(self):
        self.assertEqual(None, second_smallest_optimized([9]))


if __name__ == "__main__":
    unittest.main()
