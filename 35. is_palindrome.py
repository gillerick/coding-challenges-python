import unittest


def is_palindrome_one_liner(word):
    word = word.lower()
    return word == word[::-1]
    # a[::3] means every third element of the sequence, therefore [::-1] means every element of the sequence,
    # from the last one


# O(n) time | O(1) space
def is_palindrome_two_pointer(word):
    left_idx = 0
    right_idx = len(word) - 1

    while left_idx < right_idx:
        if word[left_idx] != word[right_idx]:
            return False
        else:
            left_idx += 1
            right_idx -= 1
    return True


# O(n/2) ~ O(n) time | O(n/2) ~ O(n) space
def is_palindrome_recursive(word, i=0):
    j = len(word) - 1 - i
    if i >= j:
        return True
    return is_palindrome_recursive(word, i + 1) and word[j] == word[i]


# O(n) time | O(n) space
def is_palindrome_iterative(word):
    reversed_chars = []
    for i in reversed(range(len(word))):
        reversed_chars.append(word[i])
    return word == "".join(reversed_chars)


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(True, is_palindrome_one_liner("racecar"))
        self.assertEqual(False, is_palindrome_one_liner("cow"))

    def test_is_palindrome_two_pointer(self):
        self.assertEqual(True, is_palindrome_two_pointer("racecar"))
        self.assertEqual(False, is_palindrome_two_pointer("cow"))

    def test_is_palindrome_recursive(self):
        self.assertEqual(True, is_palindrome_recursive("racecar"))
        self.assertEqual(False, is_palindrome_recursive("cow"))

    def test_is_palindrome_iterative(self):
        self.assertEqual(True, is_palindrome_iterative("racecar"))
        self.assertEqual(False, is_palindrome_iterative("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(is_palindrome_one_liner(str_input))
