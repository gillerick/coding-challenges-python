import unittest


def nth_prime(n):
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
            if prime > candidate ** 0.5:
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes[-1]


def nth_prime_dp(n):
    primes = [2]
    candidate = 3
    is_prime = [True] * (10 ** 6)
    while len(primes) < n:
        if is_prime[candidate]:
            primes.append(candidate)
            for multiple in range(candidate * 2, 10 ** 6, candidate):
                is_prime[multiple] = False
        candidate += 2
    return primes[-1]


class TestNthPrime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(2, nth_prime(1))
        self.assertEqual(11, nth_prime(5))
        self.assertEqual(29, nth_prime(10))
        self.assertEqual(23, nth_prime(9))
        self.assertEqual(541, nth_prime(100))

    def test_nth_prime_dp(self):
        self.assertEqual(2, nth_prime(1))
        self.assertEqual(11, nth_prime(5))
        self.assertEqual(29, nth_prime(10))
        self.assertEqual(23, nth_prime(9))
        self.assertEqual(541, nth_prime(100))


if __name__ == "__main__":
    unittest.main()
