import re


def counter(word, text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counted = 0

    for i in re.finditer(word, text):
        # word at the first index of the string
        if i.start() == 0:
            if i.end() < len(text) - 1 and text[i.end()] not in alphabet:
                counted += 1
            elif i.end() == len(text):
                counted += 1

        # word at the end of the string
        elif i.end() == len(text):
            if i.start() > 0 and text[i.start() - 1] not in alphabet:
                counted += 1

        # word in neither at the first nor the end
        else:
            if text[i.start() - 1] not in alphabet and text[i.end()] not in alphabet:
                counted += 1
    return counted


text = input().lower()
word = input().lower()
count = 0
if word != word[::-1]:
    word_reverse = word[::-1]
    count += counter(word_reverse, text)

count += counter(word, text)

print(count)

