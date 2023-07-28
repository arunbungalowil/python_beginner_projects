from list_words import words
import random


def get_valid_word(words):
    word = random.choice(words)  # choose words randomly from the list

    while "-" in word or " " in word:
        word = random.choice(words)
    return word
def hangman():
    word = get_valid_word(words)
    print(word)

hangman()
