def unique_combinations(s):
    count = 0
    for i in range(1, len(s)):
        for j in range(i + 1, len(s)):
            a, b, c = s[:i], s[i:j], s[j:]
            if (a + b != b + c) and (b + c != c + a) and (c + a != a + b):
                count += 1
    return count


if __name__ == "__main__":
    s = str(input())
    print(unique_combinations())
