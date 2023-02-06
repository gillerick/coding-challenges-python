import unittest


def valid_parenthesis(string_input):
    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}  # keys -> closing, values -> opening
    for i in range(len(string_input)):
        character = string_input[i]
        if character in brackets.values():
            stack.append(character)
        elif character in brackets.keys():
            if not stack or stack.pop() != brackets[character]:
                return False
    return not stack


class TestValidParenthesis(unittest.TestCase):
    def test_valid_parenthesis(self):
        self.assertEqual(True, valid_parenthesis("([])(){}(())()()"))
        self.assertEqual(False, valid_parenthesis("(["))
        self.assertEqual(True, valid_parenthesis("()"))


if __name__ == "__main__":
    unittest.main()
