import unittest


def reverse_words_in_string(string):
    string = string.split()
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        string[left_idx], string[right_idx] = string[right_idx], string[left_idx]
        left_idx += 1
        right_idx -= 1
    return " ".join(string)


class TestReverseWordsInString(unittest.TestCase):
    def test_reverse_words_in_string(self):
        self.assertEqual("blue is sky the", reverse_words_in_string("the sky is blue"))
        self.assertEqual("world hello", reverse_words_in_string("hello world"))
        self.assertEqual("world hello", reverse_words_in_string("  hello world  "))


if __name__ == "__main__":
    unittest.main()
