import unittest
import sys


def smallest_difference(array_one, array_two):
    smallest = sys.maxsize
    smallest_nums = []
    for i in range(len(array_one)):
        first_element = array_one[i]
        for j in range(len(array_two)):
            second_element = array_two[j]
            difference = absolute_diff(first_element, second_element)
            if difference < smallest:
                smallest = difference
                smallest_nums = [first_element, second_element]
    return smallest_nums


def absolute_diff(first, second):
    if first < 0 and second < 0:
        return abs(abs(first) - abs(second))
    elif first > 0 and second > 0:
        return abs(first - second)
    else:
        return abs(first) + abs(second)


class TestSmallestDifference(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual([28, 26], smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))


if __name__ == "__main__":
    unittest.main()
