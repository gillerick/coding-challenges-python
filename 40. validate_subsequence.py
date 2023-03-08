import unittest


def validate_subsequence(array, subsequence):
    seq_index = 0
    for i in range(len(array)):
        if array[i] == subsequence[seq_index]:
            seq_index += 1
    return seq_index == len(subsequence)


def validate_subsequence_while_loop(array, subsequence):
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
        self.assertEqual(True, validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10]))

    def test_validate_subsequence_while_loop(self):
        self.assertEqual(True,
                         validate_subsequence_while_loop([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]))
        self.assertEqual(True, validate_subsequence_while_loop([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10]))


if __name__ == "__main__":
    unittest.main()
