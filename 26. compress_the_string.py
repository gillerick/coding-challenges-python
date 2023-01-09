def compress_string(s: str):
    output = []
    for i in range(len(s)):
        count = 0
        for j in range(1, len(s)):
            if s[i] == s[j]:
                count += 1
        output.append((count, s[i]))
    return output


if __name__ == "__main__":
    s = input().strip()
    print(compress_string(s))
