def activity_notifications(expenditure: list[int], d: int):
    pass


if __name__ == "__main__":
    n, d = input().split()
    expenditure = list(map(int, input().rstrip().split()))[:n]

    print(activity_notifications(expenditure, d))
