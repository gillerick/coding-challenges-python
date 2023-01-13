# Given an array a, your task is to apply the following mutation to it:
#
# Array a mutates into a new array b of the same length
# For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
# For example, b[0] equals 0 + a[0] + a[1]
def solution(a):
    b = []
    l = len(a)
    if l == 1:
        return a
    else:
        b.insert(0, a[0] + a[1])
        b.insert(l - 1, a[-2] + a[-1])

        for i in range(1, l - 1):
            b.insert(i, a[i - 1] + a[i] + a[i + 1])
        return b


if __name__ == "__main__":
    a = [4, 0, 1, -2, 3]
    print(solution(a))
