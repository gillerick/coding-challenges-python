from array_stack import ArrayStack


def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))  # new lines will be re-inserted when writing
    original.close()

    #     We overwrite with contents in LIFO order
    output = open(filename, 'w')  # re-opening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()


if __name__ == "__main__":
    reverse_file('original.txt')
