import random


def rock_paper_scissor():
    while True:
        choices = ('rock', 'paper', 'scissor') # created a tuple of choice
        computer_choice = random.choice(choices) # by using choice function of random module select one choice
        # print(computer_choice)

        for choice in choices: # iterating over the choice for printing
            print("*", choice)
        user_input = input('Enter one choice or press q to quit').lower() # accepting user input

        if user_input == 'q':
            break
        elif user_input not in choices:
            print('Please select choice in the list')
            continue
        elif user_input == computer_choice:
            print('It is a tie')
            match_continue = input('Do you wan to continue press y/n').lower()
            if match_continue == 'y':
                continue
            else:
                break
        elif (user_input == 'rock' and computer_choice == 'scissor') or \
             (user_input == 'paper' and computer_choice == 'rock') or \
             (user_input == 'scissor' and computer_choice == 'paper'):
            print('You win the game')
            match_continue = input('Do you wan to continue press y/n').lower()
            if match_continue == 'y':
                continue
            else:
                break
        else:
            print('You lose the game')
            break


rock_paper_scissor()



