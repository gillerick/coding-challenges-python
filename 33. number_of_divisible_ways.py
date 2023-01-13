# You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two
# different indices i < j, such that a[i] + a[j] is divisible by k

def solution(a, k):
    count = 0
    if k > max(a):
        k = max(a) + 1
    remainder_count = [0] * k
    for i in range(len(a)):
        remainder_count[a[i] % k] += 1
    count += (remainder_count[0] * (remainder_count[0] - 1)) // 2
    for i in range(1, (k + 1) // 2):
        if i != k - i:
            count += remainder_count[i] * remainder_count[k - i]
    if k % 2 == 0:
        count += (remainder_count[k // 2] * (remainder_count[k // 2] - 1)) // 2
    return count
