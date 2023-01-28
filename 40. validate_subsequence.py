import unittest


def validate_subsequence(array, subsequence):
    seq_index = 0
    for i in range(len(array)):
        if array[i] == subsequence[seq_index]:
            seq_index += 1
    return seq_index == len(subsequence)


class TestValidateSubsequence(unittest.TestCase):
    def test_validate_subsequence(self):
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]))
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10]))


if __name__ == "__main__":
    unittest.main()
