import unittest


def container_with_most_water(height: list[int]) -> int:
    maximum_area = 0
    left_idx = 0
    right_idx = len(height) - 1
    while left_idx < right_idx:
        length = right_idx - left_idx
        left_height = height[left_idx]
        right_height = height[right_idx]
        current_area = length * min(right_height, left_height)
        maximum_area = max(current_area, maximum_area)

        if left_height > right_height:
            right_idx -= 1
        elif right_height > left_height:
            left_idx += 1
        else:
            left_idx += 1
            right_idx -= 1

    return maximum_area


class TestContainerWithMostWater(unittest.TestCase):
    def test_container_with_most_water(self):
        self.assertEqual(49, container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, container_with_most_water([1, 1]))
        self.assertEqual(2, container_with_most_water([1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
