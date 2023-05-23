#!/usr/bin/python3
given_word = "trumpet and"
input_list = []
word = ""
word_len = (len(given_word))
for letter in range(0, len(given_word)):
    if letter == (len(given_word) - 1):
        word += given_word[letter]
        input_list.append(word)
    else:
        if given_word[letter] != " ":
            word += given_word[letter]
        else:
            input_list.append(word)
            word = ""

print(input_list)