import unittest
from itertools import combinations


def pairs(k, arr):
    n_combinations = []
    count = 0
    n_pairs = combinations(arr, 2)
    [n_combinations.append(x) for x in n_pairs]
    for i in range(0, len(n_combinations)):
        if abs(n_combinations[i][0] - n_combinations[i][1]) == k:
            count += 1
    return count


def pairs_dynamic(k, arr):
    arr.sort()
    diff_sum = 0
    diffs = []
    count = 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        diffs.append(diff)
        diff_sum += diff
        while diff_sum > k:
            diff_sum -= diffs.pop(0)
        if diff_sum == k:
            count += 1
            diff_sum -= diffs.pop(0)
    return count


def pairs_complement(k, arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] + k in arr:
            count += 1
    return count


def pairs_itertools(k, arr):
    n_combinations = []
    count = 0
    for i in range(0, len(arr)):
        x = arr[i]
        for j in range(i + 1, len(arr)):
            y = arr[j]
            n_combinations.append((x, y))

    for i in range(0, len(n_combinations)):
        if abs(n_combinations[i][0] - n_combinations[i][1]) == k:
            count += 1
    return count


class TestPairs(unittest.TestCase):
    def test_pairs(self):
        self.assertEqual(pairs(2, [1, 5, 3, 4, 2]), 3)
        self.assertEqual(pairs(2, [1, 3, 5, 8, 6, 4, 2]), 5)
        self.assertEqual(pairs(1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635,
                                   491595254, 879792181, 1069262793]), 0)

    def test_pairs_dynamic(self):
        self.assertEqual(pairs_dynamic(2, [1, 5, 3, 4, 2]), 3)
        self.assertEqual(pairs_dynamic(2, [1, 3, 5, 8, 6, 4, 2]), 5)
        self.assertEqual(
            pairs_dynamic(1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635,
                              491595254, 879792181, 1069262793]), 0)

    def test_pairs_complement(self):
        self.assertEqual(pairs_complement(2, [1, 5, 3, 4, 2]), 3)
        self.assertEqual(pairs_complement(2, [1, 3, 5, 8, 6, 4, 2]), 5)
        self.assertEqual(
            pairs_complement(1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635,
                                 491595254, 879792181, 1069262793]), 0)

    def test_pairs_itertools(self):
        self.assertEqual(pairs_itertools(2, [1, 5, 3, 4, 2]), 3)
        self.assertEqual(pairs_itertools(2, [1, 3, 5, 8, 6, 4, 2]), 5)
        self.assertEqual(
            pairs_itertools(1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635,
                                491595254, 879792181, 1069262793]), 0)


if __name__ == '__main__':
    unittest.main()
