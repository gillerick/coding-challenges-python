import unittest


# O(n^2) time | O(1) time
def valid_starting_city(distances, fuel, mpg):
    cities = len(distances)

    for start_city_idx in range(cities):
        miles_remaining = 0

        for current_city_idx in range(start_city_idx, start_city_idx + cities):
            if miles_remaining < 0:
                continue

            current_city_idx = current_city_idx % cities

            fuel_from_current_city = fuel[current_city_idx]
            distance_to_next_city = distances[current_city_idx]
            miles_remaining += fuel_from_current_city * mpg - distance_to_next_city

        if miles_remaining >= 0:
            return start_city_idx


class TestValidStartingCity(unittest.TestCase):
    def test_valid_starting_city(self):
        self.assertEqual(4, valid_starting_city([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))


if __name__ == "__main__":
    unittest.main()
