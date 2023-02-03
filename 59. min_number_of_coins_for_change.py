import unittest


def min_number_of_coins_for_change(n, denoms):
    num_of_coins = [0] + [float("inf") for _ in range(n + 1)]
    for denom in denoms:
        for change in range(denom, len(num_of_coins)):
            num_of_coins[change] = min(num_of_coins[change], num_of_coins[change - denom] + 1)
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1


class TestMinNumberOfCoinsForChange(unittest.TestCase):
    def test_min_number_of_coins_for_change(self):
        self.assertEqual(3, min_number_of_coins_for_change(7, [1, 5, 10]))


if __name__ == "__main__":
    unittest.main()
