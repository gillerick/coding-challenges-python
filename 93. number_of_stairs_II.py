# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import unittest


def number_of_stairs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return number_of_stairs(n - 1) + number_of_stairs(n - 2)


class TestNumberOfStairs(unittest.TestCase):
    def test_number_of_stairs(self):
        self.assertEqual(2, number_of_stairs(2))
        self.assertEqual(3, number_of_stairs(3))
        self.assertEqual(8, number_of_stairs(5))
        self.assertEqual(21, number_of_stairs(7))


if __name__ == "__main__":
    unittest.main()
