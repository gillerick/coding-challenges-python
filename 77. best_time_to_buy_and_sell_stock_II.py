import unittest


# O(n) time | O(1) space
def best_time_to_buy_and_sell_stock_ii(prices: list[int]):
    maximum_profit = 0
    for i in range(1, len(prices)):
        potential_profit = prices[i] - prices[i - 1]
        if potential_profit > 0:
            maximum_profit += potential_profit
    return maximum_profit


class TestBestTimeToBuyAndSellStockII(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock_ii(self):
        self.assertEqual(7, best_time_to_buy_and_sell_stock_ii([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
        self.assertEqual(0, best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))


if __name__ == "__main__":
    unittest.main()
