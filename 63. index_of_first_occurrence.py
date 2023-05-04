import unittest


def index_of_first_occurrence(haystack, needle):
    n = len(haystack)

    if n == 0:
        return -1
    elif haystack == needle:
        return 0

    for i in range(n):
        pivot = 0
        while pivot < n:
            potential_needle = haystack[pivot:pivot + len(needle)]
            if potential_needle == needle:
                return pivot
            else:
                pivot += 1
    return -1


class TestIndexOfFirstOccurrence(unittest.TestCase):
    def test_index_of_first_occurrence(self):
        self.assertEqual(0, index_of_first_occurrence("sadbutsad", "sad"))
        self.assertEqual(2, index_of_first_occurrence("hello", "ll"))
        self.assertEqual(-1, index_of_first_occurrence("randomstring", "boy"))


if __name__ == "__main__":
    unittest.main()
