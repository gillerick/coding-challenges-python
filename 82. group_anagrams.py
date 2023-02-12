import unittest


# O(n*mlogm) time | O(n) space
def group_anagrams(strs: list[str]):
    anagrams = {}
    for word in strs:
        sorted_word = str(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    return list(anagrams.values())


class TestGroupAnagrams(unittest.TestCase):
    def test_group_anagrams(self):
        self.assertEqual([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
                         group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        self.assertEqual([["a"]], group_anagrams(["a"]))


if __name__ == "__main__":
    unittest.main()
