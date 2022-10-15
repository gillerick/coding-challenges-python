def solve(s):
    return ' '.join(map(str.capitalize, s.split()))


if __name__ == '__main__':
    s = "erick ogayo 454t thth5656"

    result = solve(s)

    print(result)
