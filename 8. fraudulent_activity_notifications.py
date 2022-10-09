def activity_notifications(expenditure: list[int], d: int):
    for n in range(len(expenditure)):
        notifications = 0
        days_expenditure_index = d + 1
        trailing_expenses = expenditure[n:days_expenditure_index]
        median = median_calculator(trailing_expenses)
        days_expenditure = expenditure[days_expenditure_index]
        if days_expenditure >= median:
            notifications += 1

        return notifications


def median_calculator(arr: list[int]):
    sorted_arr = sorted(arr)
    length = len(arr)
    if length % 2 == 0:
        return sum(sorted_arr[(length // 2 - 1):length // 2 + 1]) / 2
    else:
        return sorted_arr[length // 2]


if __name__ == "__main__":
    n, d = map(int, input().split())
    expenditure = list(map(int, input().rstrip().split()))[:n]

    print(activity_notifications(expenditure, d))
