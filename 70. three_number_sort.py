import unittest


def three_number_sort(array, order):
    pointer = 0
    for o in order:
        for j in range(pointer, len(array)):
            if array[j] == o:
                array[j], array[pointer] = array[pointer], array[j]
                pointer += 1
    return array


class TestThreeNumberSort(unittest.TestCase):
    def test_three_number_sort(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, -1, -1], three_number_sort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))


if __name__ == "__main__":
    unittest.main()
