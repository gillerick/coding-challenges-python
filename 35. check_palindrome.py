import unittest


def check_palindrome(word):
    word = word.lower()
    return word == word[::-1]
    # a[::3] means every third element of the sequence, therefore [::-1] means every element of the sequence,
    # from the last one


class TestCheckPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        self.assertEqual(True, check_palindrome("racecar"))
        self.assertEqual(False, check_palindrome("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(check_palindrome(str_input))
