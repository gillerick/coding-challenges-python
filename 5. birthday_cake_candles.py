def birthday_cake_candles(candles):
    sorted_candles = sorted(candles)
    return candles.count(sorted_candles[-1])


if __name__ == "__main__":
    candles_count = int(input())
    candles = list(map(int, input().split()))[:candles_count]
    print(birthday_cake_candles(candles))