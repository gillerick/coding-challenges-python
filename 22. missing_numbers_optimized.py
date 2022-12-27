from collections import Counter


def missingNumbers(arr, brr):
    missing_numbers = []
    d1 = Counter(arr)
    d2 = Counter(brr)
    for i in d2:
        if i not in d1:
            missing_numbers.append(i)
    for i in d1:
        if d1[i] != d2[i]:
            missing_numbers.append(i)
    print(f"{sorted(missing_numbers)}".replace("[", "").replace("]", "").replace(",", ""))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)
