import unittest


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an
# non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest
# so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be
# able to accomplish that. Help him figure out the minimum number of additional statues needed.

def perfect_statues(statues):
    return max(statues) - min(statues) - len(statues) + 1


class TestPerfectStatues(unittest.TestCase):
    def test_perfect_statues(self):
        self.assertEqual(3, perfect_statues([6, 2, 3, 8]))
        self.assertEqual(0, perfect_statues([5, 4, 6]))
        self.assertEqual(0, perfect_statues([5, 4, 6]))
        self.assertEqual(2, perfect_statues([0, 3]))


if __name__ == "__main__":
    unittest.main()
