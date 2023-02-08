import unittest


def group_anagrams(words: list[str]):
    anagrams = {}
    result = []
    for word in words:
        ordered_word = str(sorted(word))
        if ordered_word not in anagrams:
            anagrams[ordered_word] = [word]
        else:
            anagrams[ordered_word].append(word)

    for _, anagram_sets in anagrams.items():
        result.append(anagram_sets)

    return result


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        self.assertEqual([["foo"], ["flop", "olfp"], ["oy", "yo"], ["act", "cat", "tac"]],
                         group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


if __name__ == "__main__":
    unittest.main()
