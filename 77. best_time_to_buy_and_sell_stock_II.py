import unittest


# O(n) time | O(1) space
def best_time_to_buy_and_sell_stock_ii(prices: list[int]):
    maximum_profit = 0
    for i in range(1, len(prices)):
        potential_profit = prices[i] - prices[i - 1]
        if potential_profit > 0:
            maximum_profit += potential_profit
    return maximum_profit


"""We can use dynamic programming to keep track of the maximum profit we can make so far. At each step, we calculate 
the maximum profit we can make by either selling the stock on that day or not selling it. We keep updating the 
maximum profit as we iterate through the prices list. The time complexity of this solution is O(n).
"""


# O(n) time | O(1) space
def best_time_to_buy_and_sell_stock_ii_dp(prices: list[int]):
    n = len(prices)
    if n < 2:
        return 0

    dp = [0 for i in range(n)]
    dp[0] = 0
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], 0)
    return sum(dp)


"""
In this solution, we use a greedy approach to keep track of the minimum price we have seen so far and the maximum 
profit we can make by selling the stock on that day. We iterate through the prices list and update the minimum price 
and maximum profit as we go.
"""


# O(n) time | O(1) space
def best_time_to_busy_and_sell_stock_one_pass_greedy(prices: list[int]):
    maximum_profit = 0
    for i in range(1, len(prices)):
        current_price = prices[i]
        previous_price = prices[i - 1]
        if current_price > previous_price:
            maximum_profit += current_price - previous_price
    return maximum_profit


class TestBestTimeToBuyAndSellStockII(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock_ii(self):
        self.assertEqual(7, best_time_to_buy_and_sell_stock_ii([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
        self.assertEqual(0, best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))


def best_time_to_buy_and_sell_stock_ii_dp(self):
    self.assertEqual(7, best_time_to_buy_and_sell_stock_ii([7, 1, 5, 3, 6, 4]))
    self.assertEqual(4, best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
    self.assertEqual(0, best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))


def best_time_to_busy_and_sell_stock_one_pass_greedy(self):
    self.assertEqual(7, best_time_to_buy_and_sell_stock_ii([7, 1, 5, 3, 6, 4]))
    self.assertEqual(4, best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
    self.assertEqual(0, best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))


if __name__ == "__main__":
    unittest.main()
