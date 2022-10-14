def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        print(string[i:i + max_width])


if __name__ == "__main__":
    string = input()
    width = int(input())
    wrap(string, width)
