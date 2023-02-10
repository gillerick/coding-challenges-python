import unittest


# O(n*m) time | O(1) space
def three_number_sort(arr: list[int], order: list[int]):
    pointer = 0
    for o in order:
        for i in range(pointer, len(arr)):
            if arr[i] == o:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1
    return arr


# O(n) time | O(m) space
def three_number_sort_counting_sort(arr: list[int], order: list[int]):
    count = [0] * 3
    for i in arr:
        count[order.index(i)] += 1

    sorted_arr = []
    for i in range(3):
        sorted_arr.extend([order[i]] * count[i])

    return sorted_arr


# O(n) time | O(1) space
def three_number_sort_two_pointer(arr: list[int], order: list[int]):
    pointer1 = 0
    pointer2 = len(arr) - 1
    for i in range(3):
        target = order[i]
        while pointer1 <= pointer2:
            if arr[pointer1] == target:
                pointer1 += 1
            elif arr[pointer2] != target:
                pointer2 -= 1
            else:
                arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
                pointer1 += 1
                pointer2 -= 1

    return arr


class TestThreeNumberSort(unittest.TestCase):
    def test_three_number_sort(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, -1, -1], three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))

    def test_three_number_sort_two_pointer(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, -1, -1], three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))

    def test_three_number_sort_counting_sort(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, -1, -1], three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))


if __name__ == "__main__":
    unittest.main()
