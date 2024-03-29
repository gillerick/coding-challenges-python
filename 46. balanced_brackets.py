import unittest


# O(n) time | O(n) asymptotic, may be higher in practice
def balanced_brackets(string):
    bracket_pairs = {"}": "{", "]": "[", ")": "("}
    stack = []
    for character in string:
        if character in bracket_pairs.values():
            stack.append(character)
        elif character in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[character]:
                return False
    return not stack


# O(n) time | O(n) space
def balanced_brackets_opt(string):
    bracket_pairs = {"}": "{", "]": "[", ")": "("}
    stack = {}
    stack_idx = -1
    for character in string:
        if character in bracket_pairs.values():
            stack_idx += 1
            stack[stack_idx] = character
        elif character in bracket_pairs.keys():
            if not stack or stack[stack_idx] != bracket_pairs[character]:
                return False
            stack_idx -= 1
    return stack_idx == -1


class TestBalancedBrackets(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertEqual(False, balanced_brackets("{[[[[({(}))]]]]}"))
        self.assertEqual(False, balanced_brackets("()[]{}{"))
        self.assertEqual(True, balanced_brackets("([])(){}(())()()"))

    def test_balanced_brackets_optimized(self):
        self.assertEqual(False, balanced_brackets_opt("{[[[[({(}))]]]]}"))
        self.assertEqual(False, balanced_brackets_opt("()[]{}{"))
        self.assertEqual(True, balanced_brackets_opt("([])(){}(())()()"))


if __name__ == "__main__":
    unittest.main()
