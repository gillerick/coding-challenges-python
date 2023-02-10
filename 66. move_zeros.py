import unittest


# O(n) time | O(1) space
def move_zeros(arr: list[int]):
    pointer = 0
    for i in range(len(arr)):
        current_number = arr[i]
        if current_number != 0:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    return arr


# O(n) time | O(1) space
def move_zeros_two_pointer(arr: list[int]):
    left = 0
    right = 0
    while right < len(arr):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
        right += 1
    return arr


# O(n) time | O(1) space
def move_zeros_counting_approach(arr: list[int]):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual([1, 3, 12, 0, 0], move_zeros([0, 1, 0, 3, 12]))
        self.assertEqual([0], move_zeros([0]))

    def move_zeros_two_pointer(self):
        self.assertEqual([1, 3, 12, 0, 0], move_zeros([0, 1, 0, 3, 12]))
        self.assertEqual([0], move_zeros([0]))

    def move_zeros_counting_approach(self):
        self.assertEqual([1, 3, 12, 0, 0], move_zeros([0, 1, 0, 3, 12]))
        self.assertEqual([0], move_zeros([0]))


if __name__ == "__main__":
    unittest.main()
