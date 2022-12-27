def balanced_sums(arr):
    left = 0
    right = sum(arr)
    for i in range(len(arr)):
        pivot = arr[i]
        right -= pivot
        if left == right:
            print("YES")
            return
        left += pivot
    print("NO")


if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        balanced_sums(arr)
