import unittest


def first_duplicate_value(array):
    s = set()
    for num in array:
        if num in s:
            return num
        else:
            s.add(num)
    return -1


class TestFirstDuplicateValue(unittest.TestCase):
    def test_first_duplicate_value(self):
        self.assertEqual(2, first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
        self.assertEqual(-1, first_duplicate_value([]))
        self.assertEqual(-1, first_duplicate_value([1]))
        self.assertEqual(3, first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
        self.assertEqual(1, first_duplicate_value([1, 1]))


if __name__ == "__main__":
    unittest.main()
