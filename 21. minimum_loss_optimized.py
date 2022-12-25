def minimumLoss(price):
    arr = sorted(price)
    m = sum(arr)
    d = {}
    for i in range(len(price)):
        d[price[i]] = i
    temp = [0] * len(price)
    for i in range(len(price)):
        temp[i] = d[arr[i]]
    i = 0
    j = 1
    while i < len(price) and j < len(price):
        if temp[i] < temp[j]:
            i += 1
            j += 1
        else:
            if m > arr[j] - arr[i]:
                m = arr[j] - arr[i]
            i += 1
            j += 1
    print(m)


if __name__ == '__main__':
    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    minimumLoss(price)
