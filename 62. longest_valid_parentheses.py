import unittest


def longest_valid_parentheses(s):
    def is_valid(string):
        stack = []
        matchingPairs = {"}": "{", "]": "[", ")": "("}
        for char in string:
            if char in matchingPairs.values():
                stack.append(char)
            elif char in matchingPairs.keys():
                if not stack or stack.pop() != matchingPairs[char]:
                    return False

        return not stack

    max_count = 0
    for i in range(len(s)):
        pivot = i + 1
        while pivot <= len(s):
            current_sub_string = s[i:pivot]
            if is_valid(current_sub_string):
                max_count = max(max_count, len(current_sub_string))
                pivot += 1
            else:
                pivot += 1
                continue
    return max_count


def longest_valid_parentheses_optimized(s: str) -> int:
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
        self.assertEqual(4, longest_valid_parentheses("(({})"))

    def test_longest_valid_parentheses_optimized(self):
        self.assertEqual(2, longest_valid_parentheses_optimized("(()"))
        self.assertEqual(4, longest_valid_parentheses_optimized("(({})"))


if __name__ == "__main__":
    unittest.main()
