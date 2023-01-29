import unittest


# O(n) time | O(1) space
def first_non_repeating_character(string):
    frequencies = {}
    for character in string:
        frequencies[character] = frequencies.get(character, 0) + 1

    for i in range(len(string)):
        character = string[i]
        if frequencies[character] == 1:
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
