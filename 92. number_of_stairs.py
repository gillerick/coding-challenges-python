# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.
import unittest


def number_of_possible_steps_recursive(n: int):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return number_of_possible_steps_recursive(n - 1) + number_of_possible_steps_recursive(
        n - 2) + number_of_possible_steps_recursive(n - 3)


def number_of_possible_steps_dp(n):
    def count_ways(n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1

        if memo[n] > -1:
            return memo[n]
        else:
            memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
        return memo[n]

    memo = [-1] * (n + 1)
    return count_ways(n, memo)


class TestNumberOfPossibleSteps(unittest.TestCase):
    def test_number_of_possible_steps_recursive(self):
        self.assertEqual(1, number_of_possible_steps_recursive(1))
        self.assertEqual(4, number_of_possible_steps_recursive(3))
        self.assertEqual(274, number_of_possible_steps_recursive(10))

    def test_number_of_possible_steps_dp(self):
        self.assertEqual(1, number_of_possible_steps_dp(1))
        self.assertEqual(4, number_of_possible_steps_dp(3))
        self.assertEqual(274, number_of_possible_steps_dp(10))


if __name__ == "__main__":
    unittest.main()
