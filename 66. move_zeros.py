import unittest


def move_zeros(nums: list[int]):
    pivot = 0
    for i in range(len(nums)):
        current_num = nums[i]
        if current_num != 0:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            pivot += 1
    return nums


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual([1, 3, 12, 0, 0], move_zeros([0, 1, 0, 3, 12]))
        self.assertEqual([0], move_zeros([0]))


if __name__ == "__main__":
    unittest.main()
