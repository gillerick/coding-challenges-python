import unittest


def longest_word(words):
    words = filter(lambda x: str(x).isalpha(), words.split())
    return max(words, key=len)


class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        self.assertEqual("love", longest_word("I love dogs"))
        self.assertEqual("time", longest_word("fun&!! time"))
        self.assertEqual("beautiful", longest_word("a beautiful sentence^&!"))


if __name__ == "__main__":
    unittest.main()
