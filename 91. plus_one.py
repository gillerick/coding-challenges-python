import unittest


def plus_one(digits: list[int]) -> list[int]:
    final_sum = str(digits[-1] + 1)

    if len(final_sum) == 1:
        digits[-1] = int(final_sum)
    else:
        digits.pop(-1)
        digits.extend([int(final_sum[0]), int(final_sum[1])])
    return digits


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual([1, 0], plus_one([9]))
        self.assertEqual([4, 3, 2, 2], plus_one([4, 3, 2, 1]))
        self.assertEqual([1, 2, 4], plus_one([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
