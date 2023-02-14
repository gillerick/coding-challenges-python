import unittest


def search_insert(nums: list[int], target: int):
    left_idx = 0
    right_idx = len(nums) - 1
    while left_idx < right_idx:
        mid = (left_idx + right_idx) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right_idx = mid - 1
        else:
            left_idx = mid + 1

    return left_idx


class TestSearchInsert(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(0, search_insert([2, 3, 5, 6], 1))
        self.assertEqual(1, search_insert([1, 3, 5, 6], 2))
        self.assertEqual(3, search_insert([1, 8, 10, 90], 29))


if __name__ == "__main__":
    unittest.main()
