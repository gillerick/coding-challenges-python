import unittest


def remove_duplicates(nums: list[int]) -> list[int]:
    i = 0
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums


def remove_duplicates_two_pointer(nums: list[int]) -> list[int]:
    left = 0
    right = 1
    while right < len(nums) - 1:
        if nums[left] != nums[right]:
            right += 1
            left += 1
        else:
            nums.pop(left)

    return nums


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([1, 2], remove_duplicates([1, 1, 2]))
        self.assertEqual([0, 1, 2, 3, 4], remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

    def test_remove_duplicates_two_pointer(self):
        self.assertEqual([1, 2], remove_duplicates_two_pointer([1, 1, 2]))
        self.assertEqual([0, 1, 2, 3, 4], remove_duplicates_two_pointer([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    unittest.main()
