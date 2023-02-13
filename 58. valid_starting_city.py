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


"""We want to frontload the amount of gas we can store in our trip, or put another way, traverse the most gas-scarce 
portion of the journey last. We can do this by starting in the city directly after the most scarce portion. This city 
will be the solution because we have been guaranteed enough gas to complete the journey. 

Think of problem in terms of Kadane's algorithm. Here we are trying to find most negative consecutive sum, 
where the sum refers to the least amount of fuel remaining at a given city. Once we have found that, since there is 
guaranteed to be one unique solution, it will be the index after the index at which we found the most negative sum. """


# O(n) time | O(1) time
def valid_starting_city_kadane(distances, fuel, mpg):
    cities = len(distances)
    largest_negative_distance = 0
    best_starting_city_idx = 0
    current_distance_sum = 0

    for current_city_idx in range(cities):
        distance_to_next_city = distances[current_city_idx]
        fuel_from_current_city = fuel[current_city_idx]
        current_distance_sum += fuel_from_current_city * mpg - distance_to_next_city
        if largest_negative_distance > current_distance_sum:
            largest_negative_distance = current_distance_sum
            best_starting_city_idx = (current_city_idx + 1) % cities

    return best_starting_city_idx


class TestValidStartingCity(unittest.TestCase):
    def test_valid_starting_city(self):
        self.assertEqual(4, valid_starting_city([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))

    def test_valid_starting_city_kadane(self):
        self.assertEqual(4, valid_starting_city_kadane([5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10))


if __name__ == "__main__":
    unittest.main()
