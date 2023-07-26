import random

computer_number = random.randint(1, 10)
#  print(computer_number)
guesses = 0

print('You can try five times')

while True:
    try:
        user_input = int(input('Enter a number through 1 -10'))
    except ValueError:
        print('Please enter a number')
    else:
        guesses += 1
        if guesses == 5:
            print('You reached maximum chance')
            break
        elif user_input > computer_number:
            print(f'Number you entered {user_input} is greater than the number')
            print(f'you have {5 - guesses} chance left')
        elif user_input < computer_number:
            print(f'Number you entered {user_input} is smaller than the number')
            print(f'you have {5 - guesses} chance left')
        else:
            print('You entered the correct number')
            print(f'you took {guesses} chances'.upper())
            break
