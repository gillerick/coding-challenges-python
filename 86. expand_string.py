import unittest

"""
expand the given input string in the following way
3[a] = aaa
3[a2[b]] = abbabbabb
2[cd] = cdcd
"""


def expand_string(input_string: str) -> str:
    stack = []
    i = 0
    while i < len(input_string):
        if input_string[i].isdigit():
            num = ''
            while input_string[i].isdigit():
                num += input_string[i]
                i += 1
            # Push the number onto the stack
            stack.append(int(num))
        elif input_string[i] == "[":
            stack.append('[')
            i += 1
        elif input_string[i] == ']':
            nested = ''
            while isinstance(stack[-1], str):
                nested = stack.pop() + nested
            num = stack.pop()
            # Expand the nested string and push it onto the stack
            stack.append(nested * num)
            i += 1
        else:
            # # Push the character onto the stack
            stack.append(input_string[i])
            i += 1
    return ''.join(stack).replace('[', '')


class TestExpandString(unittest.TestCase):
    def test_expand_string(self):
        self.assertEqual("aaa", expand_string("3[a]"))
        self.assertEqual("abbabbabb", expand_string("3[a2[b]]"))
        self.assertEqual("cdcd", expand_string("2[cd]"))


if __name__ == "__main__":
    unittest.main()
