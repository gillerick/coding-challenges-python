from itertools import groupby


def compress_string(s: str):
    for x, y in groupby(s):
        print((len(list(y)), int(x)), end=' ')


if __name__ == "__main__":
    s = input().strip()
    compress_string(s)
