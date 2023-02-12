import unittest


def lexicographical_numbers(n: int) -> list[int]:
    nums = [i for i in range(1, n + 1)]
    nums = sorted(nums, key=lambda num: str(num))
    return nums


class TestLexicographicalNumbers(unittest.TestCase):
    def test_lexicographical_numbers(self):
        self.assertEqual([1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], lexicographical_numbers(13))
        self.assertEqual([1, 2], lexicographical_numbers(2))
        self.assertEqual([1], lexicographical_numbers(1))
        self.assertEqual([], lexicographical_numbers(0))


if __name__ == "__main__":
    unittest.main()
