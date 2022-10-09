from bisect import bisect_left, insort_left

n, d = map(int, input().split())
t = list(map(int, input().split()))
notifications = 0

lastd = sorted(t[:d])


def median_calculator():
    return lastd[d // 2] if d % 2 == 1 else ((lastd[d // 2] + lastd[d // 2 - 1]) / 2)


for i in range(d, n):
    if t[i] >= 2 * median_calculator():
        notifications += 1
    del lastd[bisect_left(lastd, t[i - d])]
    insort_left(lastd, t[i])
print(notifications)
