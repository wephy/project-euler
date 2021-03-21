# Coded triangle numbers

from string import ascii_lowercase


def triangle_gen():
    n = len(triangle_numbers) + 1
    triangle_numbers.append(0.5 * n * (n + 1))


triangle_numbers = []
triangle_gen()

with open("p042_words.txt") as data:
    words_data = data.readlines()
words = eval(words_data[0])

triangle_word_count = 0
for word in words:
    word_value = 0
    for char in word.lower():
        word_value += ascii_lowercase.index(char) + 1
    while word_value > triangle_numbers[-1]:
        triangle_gen()
    if word_value in triangle_numbers:
        triangle_word_count += 1

print(triangle_word_count)