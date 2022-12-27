def pairs(k, arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] + k in arr:
            count += 1
    print(count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    pairs(k, arr)
