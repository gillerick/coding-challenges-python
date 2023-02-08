import unittest


def longest_path(str_array: list[str]) -> int:
    # 1. Construct a matrix from the array passed
    # 2. Loop through the matrix from the first cell to the last cell
    # 3. Have a variable that keeps track of the longest path

    # Helper function that searches through matrix using Depth First Search technique
    def dfs(x, y, previous):
        nonlocal longestPath
        # Handle base case(s)
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= previous:
            return 0

        currentLength = 1 + max(dfs(x - 1, y, matrix[x][y]),
                                dfs(x + 1, y, matrix[x][y]),
                                dfs(x, y - 1, matrix[x][y]),
                                dfs(x, y + 1, matrix[x][y]))

        # Update the longest path
        longestPath = max(longestPath, currentLength)
        return currentLength

    # We cast this to an int as it a string from the input
    matrix = [[int(x) for x in row] for row in str_array]
    longestPath = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # We initialize the previous longest path to the smallest number since we are starting the iteration
            dfs(i, j, float('-inf'))
            # Here, we subtract 1 since the path length is one less the number of cells in the connection
    return longestPath - 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(5, longest_path(["12256", "56219", "43215"]))
        self.assertEqual(3, longest_path(["345", "326", "221"]))


if __name__ == "__main__":
    unittest.main()
