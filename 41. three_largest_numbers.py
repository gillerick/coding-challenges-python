import unittest


def three_largest_numbers(array):
    three_largest = [None] * 3
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)


def shift_and_update(arr, num, idx):
    for i in range(idx + 1):
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i + 1]


class TestThreeLargestNumbers(unittest.TestCase):
    def test_three_largest_numbers(self):
        self.assertEqual([18, 141, 541], three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
        self.assertEqual([11, 43, 55], three_largest_numbers([55, 43, 11, 3, -3, 10]))
        self.assertEqual([7, 7, 7], three_largest_numbers([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
        self.assertEqual([-2, -1, 7], three_largest_numbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))


if __name__ == "__main__":
    unittest.main()
