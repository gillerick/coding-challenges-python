import unittest


def container_with_most_water(height: list[int]) -> int:
    maximum_area = 0
    start_height = height[0]
    length = 0
    for i in range(1, len(height)):
        length += 1
        current_height = height[i]
        current_area = length * min(current_height, start_height)
        if maximum_area < current_area:
            maximum_area = current_area
            if current_height > start_height:
                start_height = current_height
                length -= 1
        else:
            continue

    return maximum_area


class TestContainerWithMostWater(unittest.TestCase):
    def test_container_with_most_water(self):
        self.assertEqual(49, container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        self.assertEqual(1, container_with_most_water([1, 1]))
        self.assertEqual(2, container_with_most_water([1, 2, 1]))


if __name__ == "__main__":
    unittest.main()
