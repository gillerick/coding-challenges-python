import unittest


def longest_valid_parentheses(s: str) -> int:
    max_length = 0

    left_idx, right_idx = 0, 0
    # traverse the string from left to right
    for i in range(len(s)):
        if s[i] == '(':
            left_idx += 1
        else:
            right_idx += 1
        if left_idx == right_idx:  # valid balanced parantheses substring
            max_length = max(max_length, left_idx * 2)
        elif right_idx > left_idx:  # invalid case as ')' is more
            left_idx = right_idx = 0

    left_idx, right_idx = 0, 0
    # traverse the string from right to left
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            left_idx += 1
        else:
            right_idx += 1
        if left_idx == right_idx:  # valid balanced parantheses substring
            max_length = max(max_length, left_idx * 2)
        elif left_idx > right_idx:  # invalid case as '(' is more
            left_idx = right_idx = 0
    return max_length


class TestLongestValidParentheses(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        self.assertEqual(2, longest_valid_parentheses("(()"))


if __name__ == "__main__":
    unittest.main()
