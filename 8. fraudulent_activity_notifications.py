def activity_notifications(expenditure: list[int], d: int):
    pass


def median_calculator(arr: list[int]):
    sorted_arr = sorted(arr)
    length = len(arr)
    if length % 2 == 0:
        return sum(sorted_arr[(length // 2 - 1):length // 2 + 1]) / 2
    else:
        return sorted_arr[length // 2]


if __name__ == "__main__":
    n, d = input().split()
    expenditure = list(map(int, input().rstrip().split()))[:n]

    print(activity_notifications(expenditure, d))
