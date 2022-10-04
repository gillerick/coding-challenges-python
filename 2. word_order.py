def word_order():
    words = []
    temp = {}
    n = int(input())
    for i in range(n):
        words.append(input())
    for word in words:
        temp[word] = 0
    for word in words:
        temp[word] += 1

    unique_count = len(temp)
    print(unique_count)
    for v in temp.values():
        print(v, end=" ")


if __name__ == "__main__":
    word_order()
