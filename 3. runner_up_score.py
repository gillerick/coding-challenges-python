if __name__ == "__main__":
    array_size = int(input())
    scores = list(map(int, input().split(" ")))[:array_size]

    print(sorted(scores)[-2])