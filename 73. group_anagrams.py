import unittest


# O (w * n * log(n)) time | O(wn) space
# w - number of words, n - length of longest word
def group_anagrams(words: list[str]):
    anagrams = {}
    for word in words:  # O(w)
        ordered_word = str(sorted(word))  # O(nlog(n))
        if ordered_word not in anagrams:
            anagrams[ordered_word] = [word]
        else:
            anagrams[ordered_word].append(word)

    return list(anagrams.values())


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        self.assertEqual([["foo"], ["flop", "olfp"], ["oy", "yo"], ["act", "cat", "tac"]],
                         group_anagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


if __name__ == "__main__":
    unittest.main()
