def mini_max_sum(numbers):
    maximum, minimum = sum(sorted(numbers)[1:]), sum(sorted(numbers)[:-1])
    return "{0} {1}".format(minimum, maximum)


if __name__ == '__main__':
    numbers = list(map(int, input().rstrip().split()))

    print(mini_max_sum(numbers))
