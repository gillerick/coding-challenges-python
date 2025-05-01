import unittest


def reverse_words_in_string(string):
    string_array = string.split()
    left_pointer = 0
    right_pointer = len(string_array) - 1
    while left_pointer < right_pointer:
        string_array[left_pointer], string_array[right_pointer] = string_array[right_pointer], string_array[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return " ".join(string_array)


class TestReverseWordsInString(unittest.TestCase):
    def test_reverse_words_in_string(self):
        self.assertEqual("blue is sky the", reverse_words_in_string("the sky is blue"))
        self.assertEqual("world hello", reverse_words_in_string("hello world"))
        self.assertEqual("world hello", reverse_words_in_string("  hello world  "))


if __name__ == "__main__":
    unittest.main()
