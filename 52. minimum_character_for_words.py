import unittest


def minimum_character_for_words(words_array):
    characters = {}
    for word in words_array:
        for character in word:
            current_character_count = characters.get(character, 0)
            characters[character] = + 1
            new_character_count = characters.get(character, 0)
            characters[character] = max(current_character_count, new_character_count)

    return characters


class TestMinimumCharacterForWords(unittest.TestCase):
    def test_minimum_character_for_words(self):
        self.assertEqual(["!", "a", "d", "d", "e", "e", "h", "i", "m", "s", "t", "t"],
                         minimum_character_for_words(["this", "that", "did", "deed", "them!", "a"]))


if __name__ == "__main__":
    unittest.main()
