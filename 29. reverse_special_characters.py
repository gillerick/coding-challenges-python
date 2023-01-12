def reverse_string_special_characters(s):
    s = list(s)
    i, j = 0, len(s) - 1
    special = "%&*"
    while i < j:
        if s[i] in special:
            i += 1
        elif s[j] in special:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)


if __name__ == "__main__":
    s = input().strip()
    print(reverse_string_special_characters(s))
