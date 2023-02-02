import unittest


def merge_overlapping_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval  # currentIntervalEnd = currentInterval[1]
        next_interval_start, next_interval_end = next_interval  # nextIntervalStart, nextIntervalEnd = nextInterval[0], nextInterval[1]

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals


class TestMergeOverlappingIntervals(unittest.TestCase):
    def test_merge_overlapping_intervals(self):
        self.assertEqual([[1, 2], [3, 8], [9, 10]],
                         merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
        self.assertEqual([[1, 8], [9, 10]],
                         merge_overlapping_intervals([[1, 3], [2, 8], [9, 10]]))


if __name__ == "__main__":
    unittest.main()
