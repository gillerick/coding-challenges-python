import unittest


# O(n^2 + m) time | O(n+m) space
def pattern_matcher(pattern, string):
    # Handle base case where pattern is longer than string
    if len(pattern) > len(string):
        return []
    new_pattern = get_new_pattern(pattern)
    did_switch = new_pattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    first_y_pos = get_counts_and_first_y_position(new_pattern, counts)
    if counts["y"] != 0:
        for len_of_x in range(1, len(string)):
            len_of_y = (len(string) - len_of_x * counts["x"]) / counts["y"]
            if len_of_y <= 0 or len_of_y % 1 != 0:
                continue
            len_of_y = int(len_of_y)
            y_idx = first_y_pos * len_of_x
            x = string[:len_of_x]
            y = string[y_idx:y_idx + len_of_y]
            potential_match = map(lambda char: x if char == "x" else y, new_pattern)
            if string == "".join(potential_match):
                return [x, y] if not did_switch else [y, x]
    else:
        len_of_x = len(string) / counts["x"]
        if len_of_x % 1 == 0:
            len_of_x = int(len_of_x)
            x = string[:len_of_x]
            potential_match = map(lambda char: x, new_pattern)
            if string == "".join(potential_match):
                return [x, ""] if not did_switch else ["", x]
    return []


def get_new_pattern(pattern):
    pattern_letters = list(pattern)
    if pattern[0] == "x":
        return pattern_letters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", pattern_letters))


def get_counts_and_first_y_position(pattern, counts):
    first_y_pos = None
    for i, char in enumerate(pattern):
        counts[char] += 1
        if char == "y" and first_y_pos is None:
            first_y_pos = 1
    return first_y_pos


class TestPatternMatcher(unittest.TestCase):
    def test_pattern_matcher(self):
        self.assertEqual(["go", "powerranger"], pattern_matcher("xxyxxy", "gogopowerrangergogopowerranger"))


if __name__ == "__main__":
    unittest.main()
