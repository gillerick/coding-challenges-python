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


def smallest_difference_two_pointer(array_one, array_two):
    array_one.sort()
    array_two.sort()
    smallest = sys.maxsize
    smallest_pair = []

    index_one, index_two = [0, 0]

    while index_one < len(array_one) and index_two < len(array_two):
        first, second = array_one[index_one], array_two[index_two]
        current = abs(first - second)

        if current < smallest:
            smallest = current
            smallest_pair = [first, second]
        if first > second:
            index_two += 1
        else:
            index_one += 1

    return smallest_pair


class TestSmallestDifference(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual([28, 26], smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))

    def smallest_difference_two_pointer(self):
        self.assertEqual([28, 26], smallest_difference_two_pointer([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))


if __name__ == "__main__":
    unittest.main()
