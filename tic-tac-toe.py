import random

board = [" "] * 10
computer_value = 'X'
human_value = 'O'


def display_board(board):
    for i in range(1, 10, 3):
        print(f'{board[i]} | {board[i + 1]} | {board[i + 2]}')

    print("-" * 10)


def check_win():
    if board[1] == board[2] == board[3] and board[3] != " ":
        return True
    if board[4] == board[5] == board[6] and board[6] != " ":
        return True
    if board[7] == board[8] == board[9] and board[9] != " ":
        return True
    if board[1] == board[4] == board[7] and board[1] != " ":
        return True
    if board[2] == board[5] == board[8] and board[8] != " ":
        return True
    if board[3] == board[6] == board[9] and board[9] != " ":
        return True
    if board[1] == board[5] == board[9] and board[9] != " ":
        return True
    if board[3] == board[5] == board[7] and board[7] != " ":
        return True
    else:
        return False


def check_draw():
    return True if board.count(" ") < 2 else False


def is_available(position):
    return True if board[position] == " " else False


def insert(position, value):
    if is_available(position):
        board[position] = value
        display_board(board)

        if check_win():
            if value == "X":
                print('Computer win the game')
                exit()
            else:
                print('You win the game')
                exit()

        if check_draw():
            print('Draw')
            exit()

    else:
        if value == "O":
            position = int(input('Not free please select another position'))
        else:
            position = random.randint(1, 9)

        insert(position, value)


def human_player(value):
    human_position = int(input('Enter the position to insert your value'))
    insert(human_position, value)


def computer(value):
    computer_position = random.randint(1, 9)
    insert(computer_position, value)


while not check_win():
    display_board(board)
    computer(computer_value)
    human_player(human_value)
