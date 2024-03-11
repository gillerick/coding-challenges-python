import unittest


# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


class TestCountSubstring(unittest.TestCase):
    def test_count_substring(self):
        self.assertEqual(2, count_substring("ABCDCDC", "CDC"))


if __name__ == "__main__":
    unittest.main()
