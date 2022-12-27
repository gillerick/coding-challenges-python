def maximum_sum(a, m):
    maximum_modulo = 0
    sub_arrays = find_sub_arrays(a)
    for i in range(0, len(sub_arrays)):
        modulo = sum(sub_arrays[i]) % m
        maximum_modulo = max(modulo, maximum_modulo)
    return maximum_modulo


def find_sub_arrays(array):
    sub_arrays = []
    for i in range(len(array)):
        for j in range(i + 1):
            sub_arrays.append(array[j:i + 1])
    return sub_arrays


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        print(maximum_sum(a, m))
