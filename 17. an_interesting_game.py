#!/bin/python3

# Example 1
# 1 3 5 7 9 [BOB]
# 1 3 [ANDY]
# 1 [BOB]
# BOB wins

# Example 2
# 7 4 6 5 9 [BOB]
# 7 4 6 5 [ANDY]
# ANDY Wins

def gaming_array(arr):
    count = 0
    while len(arr) > 0:
        # Find the index of the maximum integer in the array
        max_index = arr.index(max(arr))
        # Slice the array upto the maximum integer
        arr = arr[:max_index]
        # Increment count to know who played last (If counter is ODD, BOB played last)
        count += 1
    if count % 2 == 0:
        print("ANDY")
    else:
        print("BOB")


if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        gaming_array(arr)
