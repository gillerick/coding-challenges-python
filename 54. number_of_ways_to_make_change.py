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


def number_of_ways_to_make_change_improved(n, denominations):
    ways = [1] + [0 for _ in range(n)]
    for denomination in denominations:
        for change in range(denomination, n + 1):
            ways[change] += ways[change - denomination]

    return ways[-1]


def number_of_ways_to_make_change_greedy(n, denominations):
    denominations.sort(reverse=True)  # Sort the denominations in descending order
    count = 0  # Initialize the count of coins
    for d in denominations:
        while n >= d:
            count += 1  # Increment the count of coins
            n -= d  # Reduce the remaining amount
        if n == 0:
            break  # If the remaining amount is zero, exit the loop
    return count if n == 0 else -1  # Return the count or -1 if the amount cannot be made


class TestNumberOfWaysToMakeChange(unittest.TestCase):
    def test_number_of_ways_to_make_change(self):
        self.assertEqual(2, number_of_ways_to_make_change(6, [1, 5]))
        self.assertEqual(4, number_of_ways_to_make_change(10, [1, 5, 10, 25]))

    def test_number_of_ways_to_make_change_improved(self):
        self.assertEqual(2, number_of_ways_to_make_change_improved(6, [1, 5]))
        self.assertEqual(4, number_of_ways_to_make_change_improved(10, [1, 5, 10, 25]))

    def test_number_of_ways_to_make_change_greedy(self):
        self.assertEqual(2, number_of_ways_to_make_change_greedy(6, [1, 5]))
        self.assertEqual(1, number_of_ways_to_make_change_greedy(10, [1, 5, 10, 25]))


if __name__ == "__main__":
    unittest.main()
