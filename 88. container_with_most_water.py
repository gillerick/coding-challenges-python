import unittest


def container_with_most_water(height: list[int]) -> int:
    maximum_area = 0
    left_index = 0
    right_index = len(height) - 1
    while left_index < right_index:
        left_height = height[left_index]
        right_height = height[right_index]
        length = right_index - left_index
        current_area = min(left_height, right_height) * length
        maximum_area = max(current_area, maximum_area)

        if left_height > right_height:
            right_index -= 1
        elif right_index > left_index:
            left_index += 1
        else:
            right_index -= 1
            left_index += 1

    return maximum_area


class TestContainerWithMostWater(unittest.TestCase):
    def test_container_with_most_water(self):
        self.assertEqual(49, container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, container_with_most_water([1, 1]))
        self.assertEqual(2, container_with_most_water([1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
