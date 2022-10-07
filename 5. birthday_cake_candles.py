def birthday_cake_candles(candles):
    return candles.count(max(candles))


if __name__ == "__main__":
    candles_count = int(input())
    candles = list(map(int, input().split()))[:candles_count]
    print(birthday_cake_candles(candles))
