#!/bin/python3


def compare_triplets(a: list[int], b: list[int]):
    a_points = 0
    b_points = 0
    for i, j in zip(a, b):
        if i > j:
            a_points += 1
        elif j > i:
            b_points += 1

    print(f"{a_points} {b_points}")


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    compare_triplets(a, b)
