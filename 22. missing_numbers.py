def missingNumbers(arr, brr):
    sorted_brr = sorted(brr)
    temp = {}
    missing_numbers = []
    for number in sorted_brr:
        temp[number] = arr.count(number)
    for n in sorted_brr:
        if temp[n] != brr.count(n):
            missing_numbers.append(n)
    sorted_missing = sorted(set(missing_numbers))
    print(f"{sorted_missing}".replace("[", "").replace("]", "").replace(",", ""))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)
