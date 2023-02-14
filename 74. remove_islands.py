import unittest


def remove_islands(matrix):
    # Auxiliary data structure
    ones_connected_to_border = [[False for _ in matrix[0]] for _ in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_is_border = row == 0 or row == len(matrix) - 1
            col_is_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_is_border or col_is_border
            if not is_border:
                continue

            if matrix[row][col] != 1:
                continue
            find_and_mark_ones_connected_to_border(matrix, row, col, ones_connected_to_border)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if ones_connected_to_border[row][col]:
                continue
            matrix[row][col] = 0

    return matrix


def find_and_mark_ones_connected_to_border(matrix, start_row, start_col, aux_matrix):
    stack = [(start_row, start_col)]

    while len(stack) > 0:
        current_position = stack.pop()
        current_row, current_col = current_position

        already_visited = aux_matrix[current_row][current_col]

        if already_visited:
            continue

        aux_matrix[current_row][current_col] = True

        neighbours = get_neighbours(matrix, current_row, current_col)

        for neighbour in neighbours:
            row, col = neighbour

            if matrix[row][col] != 1:
                continue
            stack.append(neighbour)


def get_neighbours(matrix, row, col):
    neighbours = []
    num_rows = len(matrix)
    num_cols = len(matrix[row])

    if row - 1 >= 0:  # UP neighbour
        neighbours.append((row - 1, col))

    if row + 1 < num_rows:  # DOWN neighbour
        neighbours.append((row + 1, col))

    if col - 1 >= 0:  # LEFT neighbour
        neighbours.append((row, col - 1))

    if col + 1 < num_cols:  # RIGHT neighbour
        neighbours.append((row, col + 1))

    return neighbours


class TestRemoveIslands(unittest.TestCase):
    def test_remove_islands(self):
        self.assertEqual([[1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1],
                          [0, 0, 0, 0, 1, 0],
                          [1, 1, 0, 0, 1, 0],
                          [1, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 1]], remove_islands([[1, 0, 0, 0, 0, 0],
                                                               [0, 1, 0, 1, 1, 1],
                                                               [0, 0, 1, 0, 1, 0],
                                                               [1, 1, 0, 0, 1, 0],
                                                               [1, 0, 1, 1, 0, 0],
                                                               [1, 0, 0, 0, 0, 1]]))


if __name__ == "__main__":
    unittest.main()
