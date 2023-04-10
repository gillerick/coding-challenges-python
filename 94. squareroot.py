# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned
# integer should be non-negative as well. You must not use any built-in exponent function or operator.
import unittest


def sqrt(n):
    if n == 0:
        return 0
    for i in range(1, n + 1):
        if i * i == n:
            return i

        # This takes care of the non-perfect squares
        if i * i > n:
            return i - 1


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(2, sqrt(4))
        self.assertEqual(3, sqrt(9))
        self.assertEqual(2, sqrt(8))


if __name__ == "__main__":
    unittest.main()
