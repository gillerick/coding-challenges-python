import unittest


def search_insert(nums: list[int], target: int):
    n = len(nums)
    for i in range(n):
        current_num = nums[i]
        if current_num == target:
            return i
        elif current_num > target:
            return i
    return n


class TestSearchInsert(unittest.TestCase):
    def test_search_insert(self):
        self.assertEqual(0, search_insert([2, 3, 5, 6], 1))
        self.assertEqual(1, search_insert([1, 3, 5, 6], 2))
        self.assertEqual(4, search_insert([1, 3, 5, 6], 7))
        self.assertEqual(3, search_insert([1, 8, 10, 90], 29))


if __name__ == "__main__":
    unittest.main()
