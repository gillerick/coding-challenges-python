import unittest


# While loop solution | O(n) time | O(1) space
def validate_subsequence(array, subsequence):
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(subsequence):
        if array[arr_index] == subsequence[seq_index]:
            seq_index += 1
        arr_index += 1
    return len(subsequence) == seq_index


class TestValidateSubsequence(unittest.TestCase):
    def test_validate_subsequence(self):
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]))
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]))


if __name__ == "__main__":
    unittest.main()
