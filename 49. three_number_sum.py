import unittest


def three_number_sum(array, target_sum):
    array.sort()
    three_sums = []
    # We are looping up to the third last number
    for i in range(len(array) - 2):
        left_idx = i + 1
        right_idx = len(array) - 1
        while left_idx < right_idx:
            current = array[i]
            left = array[left_idx]
            right = array[right_idx]
            potential_sum = current + left + right
            if target_sum == potential_sum:
                three_sums.append([current, left, right])
                right_idx -= 1
                left_idx += 1
            elif potential_sum > target_sum:
                right_idx -= 1
            elif potential_sum < target_sum:
                left_idx += 1
    return three_sums


class TestThreeNumberSum(unittest.TestCase):
    def test_three_number_sum(self):
        self.assertEqual([[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]], three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0))
        self.assertEqual([[-2, 10, 49]], three_number_sum([8, 10, -2, 49, 14], 57))
        self.assertEqual([[-8, 2, 6],
                          [-8, 3, 5],
                          [-6, 0, 6],
                          [-6, 1, 5],
                          [-5, -1, 6],
                          [-5, 0, 5],
                          [-5, 2, 3],
                          [-1, 0, 1]], three_number_sum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0))
        self.assertEqual([[1, 2, 15],
                          [1, 8, 9],
                          [2, 7, 9],
                          [3, 6, 9],
                          [3, 7, 8],
                          [4, 5, 9],
                          [4, 6, 8],
                          [5, 6, 7]], three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))


if __name__ == "__main__":
    unittest.main()
