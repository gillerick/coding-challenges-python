def longest_valid_parentheses(s):
    max_count = 0
    for i in range(len(s)):
        pivot = i + 1
        while pivot <= len(s):
            current_sub_string = s[i:pivot]
            if is_valid(current_sub_string):
                max_count = max(max_count, len(current_sub_string))
                pivot += 1
            else:
                pivot += 1
                continue
    return max_count


def is_valid(string):
    stack = []
    matchingPairs = {"}": "{", "]": "[", ")": "("}
    for char in string:
        if char in matchingPairs.values():
            stack.append(char)
        elif char in matchingPairs.keys():
            if not stack or stack.pop() != matchingPairs[char]:
                return False

    return not stack
