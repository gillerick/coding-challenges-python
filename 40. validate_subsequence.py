import unittest


def validate_subsequence(array, subsequence):
    j = 0
    for i in range(len(array)):
        if array[i] == subsequence[j]:
            j += 1
        if j == len(subsequence):
            return True
    return False


class TestValidateSubsequence(unittest.TestCase):
    def test_validate_subsequence(self):
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]))


if __name__ == "__main__":
    unittest.main()
