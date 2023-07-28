from list_words import words
import random


def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)  # calling the function
    word_letters = set(word)  # convert the string into a set
    # print(word, word_letters)
    used_letters = set()
    total_chances = len(word) + 3 # total chance to the player

    while len(word_letters) > 0 and total_chances > 0:
        print_word = [letter if letter in used_letters else "-" for letter in word] # create the word
        list_to_str = "".join(print_word)
        print(f'This is the word: {list_to_str}')
        print(f'you have {total_chances} chances left in the game')
        if len(used_letters) > 0:
            print(f'used letters: {"".join(used_letters)}')
        user_letter = input('Guess the letter: ').upper()
        if user_letter.isalpha():
            total_chances -= 1
            if user_letter not in used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    print(f'letter {user_letter} not in the word')
            else:
                print(f'You already entered the letter {user_letter}')
        else:
            print('OOPS!! invalid character')

    if len(word_letters) == 0:
        print(f'you won the game, you have {total_chances} chance left')


hangman()
