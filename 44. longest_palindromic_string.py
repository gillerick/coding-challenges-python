import unittest


def longest_palindromic_string(string):
    if is_palindrome(string):
        return string

    longest = string[0]
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            current = string[i:j]
            if is_palindrome(current) and len(current) > len(longest):
                longest = current
    return longest


def is_palindrome(word):
    left_idx, right_idx = 0, len(word) - 1
    while left_idx < right_idx:
        if word[left_idx] != word[right_idx]:
            return False
        else:
            left_idx += 1
            right_idx -= 1
    return True


class TestLongestPalindromicString(unittest.TestCase):
    def test_longest_palindromic_string(self):
        self.assertEqual("noon", longest_palindromic_string("noon high it is"))
        self.assertEqual("xyzzyx", longest_palindromic_string("abaxyzzyxf"))
        self.assertEqual("a", longest_palindromic_string("a"))
        self.assertEqual("zzzzzzzzzzzzzzzzzzzz", longest_palindromic_string("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"))


if __name__ == "__main__":
    unittest.main()
