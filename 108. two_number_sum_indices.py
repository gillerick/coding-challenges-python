import unittest


# Time complexity -  O(N*2)
def two_number_sum_indices(array, target_sum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            first, second = array[i], array[j]
            if first + second == target_sum:
                return [i, j]
    return []


# Space complexity -  O(1)
# Time complexity -  O(N)
def two_number_sum_hashmap_memo_indices(array, target_sum):
    memo = {}
    for index, num in enumerate(array):
        potential_target = target_sum - num
        if potential_target in memo:
            return [memo[potential_target], index]
        else:
            memo[num] = index
    return []


class TestTwoNumberSum(unittest.TestCase):
    def test_two_number_sum(self):
        self.assertEqual([0, 1], two_number_sum_indices([3, 3], 6))
        self.assertEqual([0, 1], two_number_sum_indices([4, 6], 10))
        self.assertEqual([4, 6], two_number_sum_indices([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual([0, 2], two_number_sum_indices([4, 6, 1], 5))
        self.assertEqual([1, 3], two_number_sum_indices([4, 6, 1, -3], 3))
        self.assertEqual([7, 8], two_number_sum_indices([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))

    def test_two_number_sum_hashmap_memo(self):
        self.assertEqual([0, 1], two_number_sum_hashmap_memo_indices([3, 3], 6))
        self.assertEqual([0, 1], two_number_sum_hashmap_memo_indices([4, 6], 10))
        self.assertEqual([4, 6], two_number_sum_hashmap_memo_indices([3, 5, -4, 8, 11, 1, -1, 6], 10))
        self.assertEqual([0, 2], two_number_sum_hashmap_memo_indices([4, 6, 1], 5))
        self.assertEqual([1, 3], two_number_sum_hashmap_memo_indices([4, 6, 1, -3], 3))
        self.assertEqual([7, 8], two_number_sum_hashmap_memo_indices([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))


if __name__ == "__main__":
    unittest.main()
