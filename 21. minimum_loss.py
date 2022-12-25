def minimumLoss(price):
    minimum_loss = float('inf')
    for i in range(0, len(price)):
        for j in range(i + 1, len(price)):
            mn = price[i] - price[j]
            if minimum_loss > mn > 0:
                minimum_loss = mn
    print(minimum_loss)


if __name__ == '__main__':
    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    minimumLoss(price)
