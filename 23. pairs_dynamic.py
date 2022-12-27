def pairs(k, arr):
    arr.sort()
    diff_sum = 0
    diffs = []
    count = 0
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        diffs.append(diff)
        diff_sum += diff
        while diff_sum > k:
            diff_sum -= diffs.pop(0)
        if diff_sum == k:
            count += 1
            diff_sum -= diffs.pop(0)
    print(count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    pairs(k, arr)
