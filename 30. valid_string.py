def is_valid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs.get(char):
                return False

    return not stack


if __name__ == "__main__":
    s = input().strip()
    if is_valid(s):
        print("valid")
    else:
        print("invalid")
