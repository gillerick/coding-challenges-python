import unittest


# O(n) time | O(1) space
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


def first_unique_character_in_string_indices_approach(s: str):
    """
    In this approach, we use two lists, counts and indices, to keep track of the frequency and the first index of
    each character in the string. This allows us to avoid the need for a dictionary and reduces the time complexity
    of the first loop to O(1).

    :param s:
    :return:
    """
    n = len(s)
    counts = [0] * n
    indices = [len(s)] * n
    for i, character in enumerate(s):
        index = ord(character) - ord("a")
        counts[index] += 1
        indices[index] = min(indices[index], i)

    for i, count in enumerate(counts):
        if count == 1:
            return indices[i]
    return -1


def first_unique_character_in_string_single_integer_approach(s: str):
    """
    In this approach, we use a single integer for each character to store both its frequency and index information.
    By shifting the index to the left by 1 and adding 1, we can store the index information in the least significant
    bits, and store the frequency information in the most significant bits. This allows us to determine if a
    character is unique by checking if its count is odd. To retrieve the index, we simply shift the count right by 1.

    :param s:
    :return:
    """
    store = [0] * 26
    for i, character in enumerate(s):
        index = ord(character) - ord("a")
        store[index] += 1 << (i + 1)

    for i, count in enumerate(store):
        if count & 1:
            return count >> 1
    return -1


class TestFirstUniqueCharacterInString(unittest.TestCase):
    def test_first_unique_character_in_string(self):
        self.assertEqual(-1, first_unique_character_in_string('aabb'))
        self.assertEqual(0, first_unique_character_in_string('leetcode'))
        self.assertEqual(2, first_unique_character_in_string('loveleetcode'))

    def first_unique_character_in_string_indices_approach(self):
        self.assertEqual(-1, first_unique_character_in_string('aabb'))
        self.assertEqual(0, first_unique_character_in_string('leetcode'))
        self.assertEqual(2, first_unique_character_in_string('loveleetcode'))

    def first_unique_character_in_string_single_integer_approach(self):
        self.assertEqual(-1, first_unique_character_in_string('aabb'))
        self.assertEqual(0, first_unique_character_in_string('leetcode'))
        self.assertEqual(2, first_unique_character_in_string('loveleetcode'))


if __name__ == "__main__":
    unittest.main()
