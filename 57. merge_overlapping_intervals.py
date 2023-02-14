import unittest


# O(n log n)
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


"""
This solution works by first converting the intervals into a list of events, where each event is either a start 
time or an end time. We then sort the events based on their time. We use a count variable to keep track of the number 
of intervals that are currently active. When a new start time event is encountered, we increment the count and record 
the start time if this is the first active interval. When an end time event is encountered, we decrement the count 
and record the end time if this is the last active interval. At the end, we have a list of merged intervals. """


def merge_overlapping_intervals_sweep_line_algorithm(intervals):
    global start
    events = []
    for start, end in intervals:
        events.append((start, "start"))
        events.append((end, "end"))
    events = sorted(events)
    mergedIntervals = []
    count = 0
    for time, event in events:
        if event == "start":
            count += 1
            if count == 1:
                start = time
        else:
            count -= 1
            if count == 0:
                end = time
                mergedIntervals.append([start, end])
    return mergedIntervals


class TestMergeOverlappingIntervals(unittest.TestCase):
    def test_merge_overlapping_intervals(self):
        self.assertEqual([[1, 2], [3, 8], [9, 10]],
                         merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
        self.assertEqual([[1, 8], [9, 10]],
                         merge_overlapping_intervals([[1, 3], [2, 8], [9, 10]]))

    def test_merge_overlapping_intervals_sweep_line_algorithm(self):
        self.assertEqual([[1, 2], [3, 8], [9, 10]],
                         merge_overlapping_intervals_sweep_line_algorithm([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
        self.assertEqual([[1, 8], [9, 10]],
                         merge_overlapping_intervals_sweep_line_algorithm([[1, 3], [2, 8], [9, 10]]))


if __name__ == "__main__":
    unittest.main()
