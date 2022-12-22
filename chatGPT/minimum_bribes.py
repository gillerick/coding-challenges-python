#!/bin/python3


def minimumBribes(q):
    # Initialize the number of bribes to 0
    bribes = 0

    # Iterate through the queue in reverse order
    for i in range(len(q) - 1, -1, -1):
        # If the element is more than two positions away from its original position, it is too chaotic
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Check the elements that are within two positions of the current element
        for j in range(max(0, q[i] - 2), i):
            # If the current element is greater than a previous element, increase the bribes by 1
            if q[j] > q[i]:
                bribes += 1

    # Print the number of bribes
    print(bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
