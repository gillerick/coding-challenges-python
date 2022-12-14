def activity_notifications(expenditure: list[int], d: int):
    notifications: int = 0
    for n in range(len(expenditure) - d):
        trailing_expenses = expenditure[n:d]
        expense_median = median_calculator(trailing_expenses)
        days_expenditure = expenditure[d]
        if days_expenditure >= 2 * expense_median:
            notifications += 1
            d += 1
        else:
            d += 1

    return notifications


def median_calculator(arr):
    sorted_arr = sorted(arr)
    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return (sorted_arr[mid] + sorted_arr[mid - 1]) / 2
    else:
        return sorted_arr[mid]


if __name__ == "__main__":
    n, d = map(int, input().split())
    expenditure = list(map(int, input().rstrip().split()))

    print(activity_notifications(expenditure, d))
