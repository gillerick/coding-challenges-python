import unittest

"""
This implementation uses a backtracking algorithm to generate all possible partitions of the input string into 
palindromic substrings. The backtrack function takes three parameters: start, which is the starting index of the 
current substring; path, which is the current partition; and result, which is the list of all valid partitions. 

At each step of the backtracking, the function iterates through all possible ending indices for the current 
substring, checking if the substring from start to that index is a palindrome using the is_palindrome function. If it 
is, the function adds it to the current partition and continues the backtracking from the next index. If it's not, 
the function moves on to the next ending index.

Once the end of the string is reached, the function adds the current partition to the result. When backtracking, 
the function removes the last substring from the partition to explore other possibilities.
"""


def palindrome_partitioning(s: str):
    def is_palindrome(word: str):
        left_idx = 0
        right_idx = len(word) - 1

        while left_idx < right_idx:
            if word[left_idx] != word[right_idx]:
                return False
            else:
                right_idx -= 1
                left_idx += 1
        return True

    def backtrack(start, current_partition, valid_partitions):
        if start == len(s):
            valid_partitions.append(current_partition[:])
            return

        for i in range(start, len(s)):
            if is_palindrome(s[start:i + 1]):
                current_partition.append(s[start:i + 1])
                backtrack(i + 1, current_partition, valid_partitions)
                current_partition.pop()

    result = []
    backtrack(0, [], result)
    return result


class TestPalindromePartitioning(unittest.TestCase):
    def test_palindrome_partitioning(self):
        self.assertEqual([["a", "a", "b"], ["aa", "b"]], palindrome_partitioning("aab"))


if __name__ == "__main__":
    unittest.main()
