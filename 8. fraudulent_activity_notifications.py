def activity_notifications(expenditure: list[int], d: int):
    notifications: int = 0
    days_expenditure_index = d
    for n in range(len(expenditure) - days_expenditure_index):
        trailing_expenses = expenditure[n:days_expenditure_index]
        expense_median = median_calculator(trailing_expenses)
        days_expenditure = expenditure[days_expenditure_index]
        if days_expenditure >= 2 * expense_median:
            notifications += 1
            days_expenditure_index += 1
        else:
            days_expenditure_index += 1

    return notifications


def median_calculator(arr: list[int]):
    length = len(arr)
    index = length // 2
    sorted_arr = sorted(arr)
    if length % 2 == 0:
        return sum(sorted_arr[(index - 1):index + 1]) / 2
    else:
        return sorted_arr[length // 2]


if __name__ == "__main__":
    n, d = map(int, input().split())
    expenditure = list(map(int, input().rstrip().split()))

    print(activity_notifications(expenditure, d))
