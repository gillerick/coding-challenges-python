import unittest


def is_palindrome_one_liner(word):
    word = word.lower()
    return word == word[::-1]
    # a[::3] means every third element of the sequence, therefore [::-1] means every element of the sequence,
    # from the last one


# O(n) time | O(1) space
def is_palindrome_two_pointer(word):
    left_pointer = 0
    right_pointer = len(word) - 1
    while left_pointer < right_pointer:
        if word[left_pointer] != word[right_pointer]:
            return False
        else:
            left_pointer += 1
            right_pointer -= 1
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


# O(n) time | O(n) space
def is_palindrome_iterative_v2(word):
    length = len(word)
    for i in range(length // 2):
        # Compare character at index i with the character at the mirrored index from the end (n - 1 - i)
        if word[i] != word[length - 1 - i]:
            return False
    return True


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

    def test_is_palindrome_iterative_v2(self):
        self.assertEqual(True, is_palindrome_iterative_v2("racecar"))
        self.assertEqual(False, is_palindrome_iterative_v2("cow"))


if __name__ == "__main__":
    unittest.main()
    str_input = str(input())
    print(is_palindrome_one_liner(str_input))
