import unittest


def remove_duplicates(nums: list[int]) -> list[int]:
    i = 0
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums


class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([1, 2], remove_duplicates([1, 1, 2]))
        self.assertEqual([0, 1, 2, 3, 4], remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


if __name__ == "__main__":
    unittest.main()
