from collections import Counter
import unittest


def first_non_repeating_character(string):
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return i
    return -1


class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_first_non_repeating_character(self):
        self.assertEqual(1, first_non_repeating_character("abcdcaf"))
        self.assertEqual(6, first_non_repeating_character("faadabcbbebdf"))
        self.assertEqual(0, first_non_repeating_character("a"))
        self.assertEqual(1, first_non_repeating_character("abac"))
        self.assertEqual(7, first_non_repeating_character("lmnopqldsafmnopqsa"))


if __name__ == "__main__":
    unittest.main()
