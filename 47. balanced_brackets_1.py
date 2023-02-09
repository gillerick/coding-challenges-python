import unittest


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


class TestBalancedBrackets(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertEqual(False, balanced_brackets("{[[[[({(}))]]]]}"))
        self.assertEqual(False, balanced_brackets("()[]{}{"))
        self.assertEqual(True, balanced_brackets("([])(){}(())()()"))


if __name__ == "__main__":
    unittest.main()
