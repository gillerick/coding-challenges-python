import unittest

"""Dynamic programing O(n) space | O(nd) time"""


def number_of_ways_to_make_change(n, denominations):
    # Initialize ways array
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    for denomination in denominations:
        for amount in range(1, n + 1):
            if denomination <= amount:
                ways[amount] += ways[amount - denomination]

    return ways[n]


class TestNumberOfWaysToMakeChange(unittest.TestCase):
    def test_number_of_ways_to_make_change(self):
        self.assertEqual(2, number_of_ways_to_make_change(6, [1, 5]))
        self.assertEqual(4, number_of_ways_to_make_change(10, [1, 5, 10, 25]))


if __name__ == "__main__":
    unittest.main()
