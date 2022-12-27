def pairs(k, arr):
    n_combinations = []
    count = 0
    for i in range(0, len(arr)):
        x = arr[i]
        for j in range(i + 1, len(arr)):
            y = arr[j]
            n_combinations.append((x, y))

    for i in range(0, len(n_combinations)):
        if abs(n_combinations[i][0] - n_combinations[i][1]) == k:
            count += 1
    print(count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    pairs(k, arr)
