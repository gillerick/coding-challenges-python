#!/bin/python3


def minimumBribes(q):
    sum = 0
    for i in range(1, len(q)):
        diff = q[i - 1] - q[i]
        if diff > 0:
            sum += diff
        if diff > 2:
            print("Too chaotic")
            return
    print(sum)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
