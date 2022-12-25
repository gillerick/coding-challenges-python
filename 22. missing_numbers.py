def missingNumbers(arr, brr):
    sorted_arr = sorted(arr)
    sorted_brr = sorted(brr)
    temp = {}
    missing = []
    for number in sorted_brr:
        temp[number] = brr.count(number)
    for n in sorted_arr:
        if temp[n] != arr.count(n):
            missing.append(n)
    sorted_missing = sorted(missing)
    print(f"{set(sorted_missing)}".replace("{", "").replace("}", "").replace(",", ""))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)
