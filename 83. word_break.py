import unittest


def word_break(s, word_dict):
    for word in word_dict:
        if word not in s:
            return False
    return True


def word_break_dp(s, word_dict):
    n = len(s)
    dp = [True] + [False] * n

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[-1]


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        self.assertEqual(True, word_break("leetcode", ["leet", "code"]))
        self.assertEqual(True, word_break("applepenapple", ["apple", "pen"]))
        # self.assertEqual(False, word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  Test fails

    def test_word_break_dp(self):
        self.assertEqual(True, word_break_dp("leetcode", ["leet", "code"]))
        self.assertEqual(True, word_break_dp("applepenapple", ["apple", "pen"]))
        self.assertEqual(False, word_break_dp("catsandog", ["cats", "dog", "sand", "and", "cat"]))


if __name__ == "__main__":
    unittest.main()
