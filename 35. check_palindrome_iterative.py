import unittest


# O(n) time | O(n) space
def check_palindrome(word):
    reversed_chars = []
    for i in reversed(range(len(word))):
        reversed_chars.append(word[i])
    return word == "".join(reversed_chars)


class TestCheckPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        self.assertEqual(True, check_palindrome("racecar"))
        self.assertEqual(False, check_palindrome("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(check_palindrome(str_input))
