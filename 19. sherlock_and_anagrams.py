def generateSubstrings(word):
    substrings = {}
    for i in range(len(word)):
        for j in range(i, len(word)):
            substring = word[i:j + 1]
            if len(substring) > 1:
                substring = ''.join(sorted(substrings))
            substrings[substring] = substrings.get(substring, 0) + 1
            print(substring)
    return substrings


def sherlockAndAnagrams(s):
    # Write your code here
    substringsDict = generateSubstrings(s)
    print(substringsDict)
    anagpairs = 0
    for substring in substringsDict:
        freq = substringsDict[substring]
        anagpairs += ((freq) * (freq - 1)) // 2
    return anagpairs


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        sherlockAndAnagrams(s)
