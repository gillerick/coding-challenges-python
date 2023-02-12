import unittest


def word_break(s, word_dict):
    for word in word_dict:
        if word not in s:
            return False
    return True


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        self.assertEqual(True, word_break("leetcode", {"leet", "code"}))
        self.assertEqual(True, word_break("applepenapple", {"apple", "pen"}))


if __name__ == "__main__":
    unittest.main()
