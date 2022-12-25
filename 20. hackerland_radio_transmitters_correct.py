def hackerlandRadioTransmitters(x, k):
    arr = sorted(x)
    l = len(x)
    pot = arr[0]
    flag = True
    d = 1
    for i in range(l):
        if arr[i] - pot > k:
            if arr[i] - arr[i - 1] <= k and flag:
                pot = arr[i - 1]
                flag = False
            else:
                pot = arr[i]
                d += 1
                flag = True
    print(d)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    hackerlandRadioTransmitters(x, k)
