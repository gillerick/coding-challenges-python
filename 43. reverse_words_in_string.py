import unittest


# O(n) time | O(n) space
def reverse_words_in_string(string):
    words = []
    start = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[start:idx])
            start = idx
        elif string[start] == " ":
            words.append(" ")
            start = idx
    #         Adds last word to the words array
    words.append(string[start:])
    reverse_list(words)
    return "".join(words)


def reverse_list(list):
    start, end = 0, len(list) - 1
    # Doesn't matter whether list is odd or even, this always works
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


class TestReverseWordsInString(unittest.TestCase):
    def test_reverse_words_in_string(self):
        self.assertEqual("Words These  Reverse", reverse_words_in_string("Reverse  These Words"))


if __name__ == "__main__":
    unittest.main()
