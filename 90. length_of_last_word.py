import unittest


def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


class TestLengthOfLastWord(unittest.TestCase):
    def test_length_of_last_word(self):
        self.assertEqual(5, length_of_last_word("Hello World"))
        self.assertEqual(4, length_of_last_word("   fly me   to   the moon  "))
        self.assertEqual(6, length_of_last_word("luffy is still joyboy"))


if __name__ == "__main__":
    unittest.main()
