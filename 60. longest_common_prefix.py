import unittest


def longest_common_prefix(strs: list[str]):
    res = ""
    for a in zip(*strs):
        if len(set(a)) == 1:
            res += a[0]
        else:
            return res
    return res


class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        self.assertEqual("fl", longest_common_prefix(["flower", "flow", "flight"]))
        self.assertEqual("", longest_common_prefix(["dog", "racecar", "car"]))


if __name__ == "__main__":
    unittest.main()
