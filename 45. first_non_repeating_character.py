from collections import Counter
import unittest


def first_non_repeating_character(string):
    counts = Counter(string)
    for i in range(len(string)):
        if counts[string[i]] == 1:
            return i
    return -1


def first_non_repeating_character_inplace(string):
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return i
    return -1


# O(n) time | O(1) space
def first_non_repeating_character_hashmap(string):
    frequencies = {}
    for character in string:
        frequencies[character] = frequencies.get(character, 0) + 1

    for character, count in frequencies.items():
        if count == 1:
            return string.index(character)
    return -1


class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_first_non_repeating_character(self):
        self.assertEqual(1, first_non_repeating_character("abcdcaf"))
        self.assertEqual(6, first_non_repeating_character("faadabcbbebdf"))
        self.assertEqual(0, first_non_repeating_character("a"))
        self.assertEqual(1, first_non_repeating_character("abac"))
        self.assertEqual(7, first_non_repeating_character("lmnopqldsafmnopqsa"))

    def test_first_non_repeating_character_hashmap(self):
        self.assertEqual(1, first_non_repeating_character_hashmap("abcdcaf"))
        self.assertEqual(6, first_non_repeating_character_hashmap("faadabcbbebdf"))
        self.assertEqual(0, first_non_repeating_character_hashmap("a"))
        self.assertEqual(1, first_non_repeating_character_hashmap("abac"))
        self.assertEqual(7, first_non_repeating_character_hashmap("lmnopqldsafmnopqsa"))

    def test_first_non_repeating_character_inplace(self):
        self.assertEqual(1, first_non_repeating_character_inplace("abcdcaf"))
        self.assertEqual(6, first_non_repeating_character_inplace("faadabcbbebdf"))
        self.assertEqual(0, first_non_repeating_character_inplace("a"))
        self.assertEqual(1, first_non_repeating_character_inplace("abac"))
        self.assertEqual(7, first_non_repeating_character_inplace("lmnopqldsafmnopqsa"))


if __name__ == "__main__":
    unittest.main()
