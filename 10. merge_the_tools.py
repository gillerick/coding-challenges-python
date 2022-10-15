def merge_the_tools(string, k):
    substrings = []
    for i in range(0, len(string), k):
        tool = string[i:k + i]
        new_tool = ""
        for c in tool:
            if c not in new_tool:
                new_tool += c
        substrings.append(new_tool)
    return print("\n".join(substrings))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
