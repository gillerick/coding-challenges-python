# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
# each sock, determine how many pairs of socks with matching colors there are.

import unittest


def sales_by_match(array):
    numbers = {}
    for element in array:
        if element in numbers:
            numbers[element] += 1
        else:
            numbers[element] = 1

    pairs = 0
    for k, v in numbers.items():
        pair = v // 2
        pairs += pair

    return pairs


class TestSalesByMatch(unittest.TestCase):
    def test_sales_by_match(self):
        self.assertEqual(2, sales_by_match([1, 2, 1, 2, 1, 3, 2]))
        self.assertEqual(1, sales_by_match(["red", "black", "blue", "red", "purple"]))
        self.assertEqual(3, sales_by_match(["black", "black", "black", "red", "red", "blue", "blue", "yellow", "indigo"]))


if __name__ == "__main__":
    unittest.main()
