import unittest


def two_number_sum(array, target_sum):
    numbers = []
    for i in range(len(array)):
        for j in range(1, len(array)):
            first, second = array[i], array[j]
            if first + second == target_sum and first != second:
                numbers.append(first)
                numbers.append(second)
                return numbers
    return numbers


class TestTwoNumberSum(unittest.TestCase):
    def test_two_number_sum(self):
        self.assertEqual([11, -1], two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual([4, 6], two_number_sum([4, 6], 10))
        self.assertEqual([4, 1], two_number_sum([4, 6, 1], 5))
        self.assertEqual([6, -3], two_number_sum([4, 6, 1, -3], 3))
        self.assertEqual([8, 9], two_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))


if __name__ == "__main__":
    unittest.main()
