import unittest


def first_duplicate_value(array):
    arrays_dict = {}
    for num in array:
        if num in arrays_dict:
            # Increment count of num
            arrays_dict[num] += 1
        else:
            arrays_dict[num] = 0

        if arrays_dict[num] > 0:
            return num
    return -1


def first_duplicate_value_set(array: list[int]):
    seen = set()
    for num in array:
        if num not in seen:
            seen.add(num)
        else:
            return num
    return -1


class TestFirstDuplicateValue(unittest.TestCase):
    def test_first_duplicate_value(self):
        self.assertEqual(2, first_duplicate_value([2, 1, 5, 2, 3, 3, 4]))
        self.assertEqual(3, first_duplicate_value([2, 1, 5, 3, 3, 2, 4]))
        self.assertEqual(-1, first_duplicate_value([]))
        self.assertEqual(-1, first_duplicate_value([1]))
        self.assertEqual(1, first_duplicate_value([1, 1]))

    def test_first_duplicate_value_set(self):
        self.assertEqual(2, first_duplicate_value_set([2, 1, 5, 2, 3, 3, 4]))
        self.assertEqual(3, first_duplicate_value_set([2, 1, 5, 3, 3, 2, 4]))
        self.assertEqual(-1, first_duplicate_value_set([]))
        self.assertEqual(-1, first_duplicate_value_set([1]))
        self.assertEqual(1, first_duplicate_value_set([1, 1]))


if __name__ == "__main__":
    unittest.main()
