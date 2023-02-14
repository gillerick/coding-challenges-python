import unittest


def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for c in num:
        while stack and k > 0 and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    while stack and k > 0:
        stack.pop()
        k -= 1
    if not stack:
        return "0"
    return str(int("".join(stack)))


class TestRemoveKDigits(unittest.TestCase):
    def test_remove_k_digits(self):
        self.assertEqual("1219", remove_k_digits("1432219", 3))
        self.assertEqual("200", remove_k_digits("10200", 1))
        self.assertEqual("0", remove_k_digits("10", 2))
        self.assertEqual("0", remove_k_digits("10", 1))


if __name__ == "__main__":
    unittest.main()
