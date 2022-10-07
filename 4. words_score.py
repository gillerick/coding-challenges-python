def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    transformed_words = list(map(str, words))
    score = 0
    for word in transformed_words:
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
    n = int(input())
    words = input().split()
    print(score_words(words))

