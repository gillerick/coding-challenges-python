def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        vowels = 0
        for letter in word:
            if is_vowel(letter):
                vowels += 1
        if vowels % 2 == 0:
            score += 2
        else:
            score += 1

    return score


if __name__ == "__main__":
    no_words = int(input())
    words = list(map(str, input().split(" ")))[:no_words]
    print(score_words(words))

