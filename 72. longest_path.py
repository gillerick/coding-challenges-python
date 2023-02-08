import unittest


def longest_path(str_array: list[str]) -> int:
    def dfs(row, column, previous):
        nonlocal longestPath
        if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or matrix[row][column] <= previous:
            return 0

        currentLength = 1 + max(dfs(row - 1, column, matrix[row][column]),
                                dfs(row + 1, column, matrix[row][column]),
                                dfs(row, column - 1, matrix[row][column]),
                                dfs(row, column + 1, matrix[row][column]))

        longestPath = max(longestPath, currentLength)
        return currentLength

    matrix = [[int(x) for x in row] for row in str_array]
    longestPath = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            dfs(row, col, float('-inf'))
    return longestPath - 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, longest_path(["12256", "56219", "43215"]))
        self.assertEqual(3, longest_path(["345", "326", "221"]))


if __name__ == "__main__":
    unittest.main()
