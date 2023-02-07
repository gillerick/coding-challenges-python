import unittest


def check_permutation(s1, s2):
    letters = {}
    if len(s1) != len(s2):
        return False

    for character in s1:
        letters[character] = letters.get(character, 0) + 1

    for character in s2:
        letters[character] -= 1
        if letters[character] < 0:
            return False
    return True


class TestCheckPermutation(unittest.TestCase):
    def test_check_permutation(self):
        self.assertEqual(True, check_permutation("drool", "drool"))
        self.assertEqual(False, check_permutation("girl", "boy"))
        self.assertEqual(True, check_permutation("768", "678"))


if __name__ == "__main__":
    unittest.main()
