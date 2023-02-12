import unittest


# O(n^2) time | O(1) space - suboptimal
def best_time_to_buy_and_sell_stock(prices: list[int]):
    n = len(prices)
    maximum_profit = 0
    for i in range(n):
        right_idx = i + 1
        while right_idx < n:
            potential_profit = prices[right_idx] - prices[i]
            maximum_profit = max(maximum_profit, potential_profit)
            right_idx += 1
    return maximum_profit


# O(n) time | O(1) space - optimal
def best_time_to_buy_and_sell_stock_kadane(prices: list[int]):
    maximum_profit = 0
    minimum_buy = prices[0]
    for price in prices:
        minimum_buy = min(minimum_buy, price)
        current_profit = price - minimum_buy
        maximum_profit = max(current_profit, maximum_profit)

    return maximum_profit


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        self.assertEqual(0, best_time_to_buy_and_sell_stock([9, 8, 5, 4, 1]))
        self.assertEqual(5, best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))

    def test_best_time_to_buy_and_sell_stock_kadane(self):
        self.assertEqual(0, best_time_to_buy_and_sell_stock([9, 8, 5, 4, 1]))
        self.assertEqual(5, best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))


if __name__ == "__main__":
    unittest.main()
