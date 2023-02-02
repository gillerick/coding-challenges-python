import unittest

"""Dynamic programing O(n) space | O(nd) time"""


def number_of_ways_to_make_change(n, denominations):
    # Initialize ways array
    ways = [1] + [0 for _ in range(n)]
    for denomination in denominations:
        for change in range(denomination, n + 1):
            ways[change] += ways[change - denomination]

    return ways[-1]


class TestNumberOfWaysToMakeChange(unittest.TestCase):
    def test_number_of_ways_to_make_change(self):
        self.assertEqual(4, number_of_ways_to_make_change(10, [1, 5, 10, 25]))
        self.assertEqual(2, number_of_ways_to_make_change(6, [1, 5]))


if __name__ == "__main__":
    unittest.main()
