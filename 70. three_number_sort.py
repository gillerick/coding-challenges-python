import unittest


def three_number_sort(array, order):
    for o in order:
        pointer = 0
        for j in range(1, len(array)):
            if array[j] == o:
                array[j], array[pointer] = array[pointer], array[j]
                pointer += 1
    array.reverse()
    return array


class TestThreeNumberSort(unittest.TestCase):
    def test_three_number_sort(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, -1, -1], three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))


if __name__ == "__main__":
    unittest.main()
