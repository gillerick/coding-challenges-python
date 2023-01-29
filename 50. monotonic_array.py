import unittest


def is_monotonic(array):
    for i in range(1, len(array)):
        if is_increasing(array) and array[i - 1] > array[i]:
            return False
        else:
            if array[i - 1] < array[i]:
                return False
    return True


def is_increasing(array):
    return array[0] < array[-1]


class TestIsMonotonic(unittest.TestCase):
    def test_is_monotonic(self):
        self.assertEqual(True, is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))


if __name__ == "__main__":
    unittest.main()
