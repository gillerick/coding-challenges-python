import unittest


def haunted_houses(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                k = len(matrix) - 1
                while k < len(matrix) - 1:
                    matrix[k][j] = 0
                    k -= 1

    return [sum(x) for x in matrix]


class TestHauntedHouse(unittest.TestCase):
    def test_haunted_house(self):
        self.assertEqual(9, haunted_houses([[1, 1, 1, 0],
                                            [0, 5, 0, 1],
                                            [2, 1, 3, 10]]))


if __name__ == "__main__":
    unittest.main()
