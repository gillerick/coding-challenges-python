import unittest


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an
# non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest
# so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be
# able to accomplish that. Help him figure out the minimum number of additional statues needed.

def perfect_statues(statues):
    statue_set = set(statues)
    return max(statue_set) - min(statue_set) - len(statue_set) + 1


class TestPerfectStatues(unittest.TestCase):
    def test_perfect_statues(self):
        self.assertEqual(3, perfect_statues([6, 2, 3, 8]))
        self.assertEqual(0, perfect_statues([5, 4, 6]))
        self.assertEqual(0, perfect_statues([5, 4, 6]))
        self.assertEqual(2, perfect_statues([0, 3]))
        self.assertEqual(8, perfect_statues([5, 10, 15]))
        self.assertEqual(10, perfect_statues([-2, 10, 4]))
        self.assertEqual(0, perfect_statues([5, 4, 5]))
        self.assertEqual(0, perfect_statues([5, 5]))
        self.assertEqual(8, perfect_statues([5, 10, 5, 15]))


if __name__ == "__main__":
    unittest.main()
