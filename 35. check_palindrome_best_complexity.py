import unittest


# O(n) time | O(1) space
def is_palindrome(string):
    left_idx = 0
    right_idx = len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        else:
            left_idx += 1
            right_idx -= 1
    return True


class TestCheckPalindrome(unittest.TestCase):
    def test_check_palindrome(self):
        self.assertEqual(True, is_palindrome("racecar"))
        self.assertEqual(False, is_palindrome("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(is_palindrome(str_input))
