def playing_with_numbers(array, queries):
    temp_array = []
    for query in queries:
        for j in range(len(array)):
            summation = array[j] + query
            temp_array.append(summation)
        array = temp_array.copy()
        print(sum([abs(element) for element in temp_array]), end="\n")
        temp_array.clear()


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = list(map(int, input().rstrip().split()))

    playing_with_numbers(arr, queries)
