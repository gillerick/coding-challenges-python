import unittest


def first_unique_character_in_string(s: str):
    counts = {}
    for character in s:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1

    for character, count in counts.items():
        if count == 1:
            return s.index(character)
    return -1


class TestFirstUniqueCharacterInString(unittest.TestCase):
    def test_first_unique_character_in_string(self):
        self.assertEqual(-1, first_unique_character_in_string('aabb'))
        self.assertEqual(0, first_unique_character_in_string('leetcode'))
        self.assertEqual(2, first_unique_character_in_string('loveleetcode'))


if __name__ == "__main__":
    unittest.main()
