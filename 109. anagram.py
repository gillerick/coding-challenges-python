import unittest


# Time complexity - O(n)
def anagram_array(string_one, string_two):
    if len(string_one) != len(string_two):
        return False

    frequency_counter = [0] * 26

    for i in range(len(string_one)):
        frequency_counter[ord(string_one[i]) - ord('a')] += 1
        frequency_counter[ord(string_two[i]) - ord('a')] -= 1

    for i in range(len(string_one)):
        if frequency_counter[i] != 0:
            return False
    return True


# Time complexity - O(n)

def anagram_hashmap(string_one, string_two):
    if len(string_one) != len(string_two):
        return False

    frequency_counter = {}

    for char in string_one:
        frequency_counter[char] = frequency_counter.get(char, 0) + 1

    for char in string_two:
        if char not in frequency_counter:
            return False
        frequency_counter[char] -= 1

        if frequency_counter[char] < 0:
            return False
    return True


class TestAnagram(unittest.TestCase):
    def test_anagram_array(self):
        self.assertEqual(True, anagram_array("anagram", "nagaram"))
        self.assertEqual(True, anagram_array("rat", "tar"))
        self.assertEqual(False, anagram_array("rat", "cat"))

    def test_anagram_hashmap(self):
        self.assertEqual(True, anagram_hashmap("anagram", "nagaram"))
        self.assertEqual(True, anagram_hashmap("rat", "tar"))
        self.assertEqual(False, anagram_hashmap("rat", "cat"))


if __name__ == "__main__":
    unittest.main()
