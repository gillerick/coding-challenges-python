import unittest


def valid_parenthesis(string_input):
    stack = []
    brackets = {"]": "[", "}": "{", ")": "("}
    opening_brackets = brackets.values()
    closing_brackets = brackets.keys()
    for char in string_input:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0

    # 1. Iterate through the input and check for an opening parenthesis
    # 2. Push the opening parenthesis into the stack
    # 3. If the parenthesis is closing, then check the stack for a corresponding opening
    # 4. Remove the opening parenthesis if exists
    # 5. If no corresponding parenthesis, then we return an early False
    # 6. Finally, check if the stack is empty and return the boolean (stack is empty)


class TestValidParenthesis(unittest.TestCase):
    def test_valid_parenthesis(self):
        self.assertEqual(True, valid_parenthesis("([])(){}(())()()"))
        self.assertEqual(False, valid_parenthesis("(["))
        self.assertEqual(True, valid_parenthesis("()"))
        self.assertEqual(False, valid_parenthesis("([]"))


if __name__ == "__main__":
    unittest.main()
