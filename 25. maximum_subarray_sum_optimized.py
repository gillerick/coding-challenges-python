def maximum_sum(a, m):
    pass
    # maximum_modulo = 0
    # for i in range(len(a)):
    #     for j in range(i + 1):
    #         modulo = sum(a[j:i + 1]) % m
    #         maximum_modulo = max(modulo, maximum_modulo)
    # return maximum_modulo


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        print(maximum_sum(a, m))
