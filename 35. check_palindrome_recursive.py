import unittest


# O(n/2) ~ O(n) time | O(n/2) ~ O(n) space
def is_palindrome_recursive(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and is_palindrome_recursive(string, i + 1)


class TestCheckPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        self.assertEqual(True, is_palindrome_recursive("racecar"))
        self.assertEqual(False, is_palindrome_recursive("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(is_palindrome_recursive(str_input))
