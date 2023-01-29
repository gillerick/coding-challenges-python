import unittest
import sys


def smallest_difference(array_one, array_two):
    smallest = sys.maxsize
    smallest_nums = []
    for first in array_one:
        for second in array_two:
            difference = abs(first - second)
            if difference < smallest:
                smallest = difference
                smallest_nums = [first, second]
    return smallest_nums


class TestSmallestDifference(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual([28, 26], smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))


if __name__ == "__main__":
    unittest.main()
