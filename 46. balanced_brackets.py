import unittest


def balanced_brackets(string):
    opening = {"{": 0, "[": 0, "(": 0}
    closing = {"}": 0, "]": 0, ")": 0}
    for character in string:
        if character in opening.keys():
            opening[character] += 1
        elif character in closing.keys():
            closing[character] += 1

    for opening_count, closing_count in zip(opening.values(), closing.values()):
        if opening_count != closing_count:
            return False
    return True


class TestBalancedBrackets(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertEqual(False, balanced_brackets("{[[[[({(}))]]]]}"))
        self.assertEqual(False, balanced_brackets("()[]{}{"))
        self.assertEqual(True, balanced_brackets("([])(){}(())()()"))


if __name__ == "__main__":
    unittest.main()
