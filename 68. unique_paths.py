import unittest


def unique_paths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    if m == 1 and n == 1:
        return 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = 0
                # last position in the grid set it to zero..
            elif i == m - 1:
                dp[i][j] = 1
                # check the edge cases...
            elif j == n - 1:
                dp[i][j] = 1
                # check the edge cases...
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    return dp[0][0]


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths(self):
        self.assertEqual(28, unique_paths(3, 7))
        self.assertEqual(1820, unique_paths(5, 13))
        self.assertEqual(3, unique_paths(3, 2))
        self.assertEqual(1, unique_paths(1, 1))
        self.assertEqual(2, unique_paths(2, 2))
        self.assertEqual(3, unique_paths(2, 3))
        self.assertEqual(6, unique_paths(3, 3))
        self.assertEqual(10, unique_paths(4, 3))
        self.assertEqual(20, unique_paths(4, 4))


if __name__ == "__main__":
    unittest.main()
