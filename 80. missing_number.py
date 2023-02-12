import unittest


def missing_number(nums):
    for i in range(max(nums)):
        if i not in nums:
            return i
    return 0


class TestMissingNumber(unittest.TestCase):
    def test_missing_number(self):
        self.assertEqual(2, missing_number([0, 1, 3]))
        self.assertEqual(8, missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    unittest.main()
