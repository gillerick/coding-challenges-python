def minimum_bribes(q):
    # Initialize an array to keep track of the number of bribes for each position
    bribes = [0] * (len(q) + 1)

    # Iterate through the queue
    for i, p in enumerate(q):
        # If the element is more than two positions away from its original position, it is too chaotic
        if p - (i + 1) > 2:
            print("Too chaotic")
            return

        # Increment the number of bribes for the current position and all subsequent positions
        for j in range(p, len(bribes)):
            bribes[j] += 1

    # Print the sum of the bribes
    print(sum(bribes))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimum_bribes(q))
