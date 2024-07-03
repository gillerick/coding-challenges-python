import unittest


# O(n log(n))
def second_smallest(nums):
    if len(nums) == 1:
        return None

    return sorted(nums)[1]


class SecondSmallest(unittest.TestCase):
    def test_second_smallest(self):
        self.assertEqual(2, second_smallest([8, 9, 2, 3]))


if __name__ == "__main__":
    unittest.main()
