def missingNumbers(arr, brr):
    temp = {}
    temp1 = {}
    missing = []
    for number in brr:
        temp[number] = brr.count(number)
    for n in arr:
        temp1[n] = arr.count(n)
    for n in arr:
        if temp[n] != temp1[n]:
            missing.append(n)
    sorted(missing)
    print(f"{set(missing)}".replace("{", "").replace("}", "").replace(",", ""))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    missingNumbers(arr, brr)
