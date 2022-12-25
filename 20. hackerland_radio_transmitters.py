import math


def hackerlandRadioTransmitters(x, k):
    transmitter_range = k * 2 + 1
    houses_range = max(x) - min(x) + 1
    print(math.ceil(houses_range / transmitter_range))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    hackerlandRadioTransmitters(x, k)
