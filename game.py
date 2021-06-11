

def display_board(board):
    print (board[0] +'|'+board[1]+ '|'+board[2])
    print (board[3] +'|'+board[4]+ '|'+board[5])
    print (board[6] +'|'+board[7]+ '|'+board[8])


def player_select():

    marker = input('Player One please select X or O: ')
    if marker == 'X' or marker == 'x':
        p1 = 'X'
        p2 = 'O'
        print('Player One is X, and Player two is O')
    elif marker == 'O' or marker == 'o':
        p1 = 'O'
        p2 = 'X'
        print('Player One is O, and Player two is X')
    return p1, p2


def tie_check(board):
    if "_" in board[0:]:
        return False
    else:
        display_board(board)
        print('Tie Game')
        return True


def win_check(board):

    winner = " "

    if board[0] == board[1] == board[2] == (p1) or board[0] == board[1] == board[2] == (p2):
        winner = board[0]
    elif board[3] == board[4] == board[5] == (p1) or board[3] == board[4] == board[5] == (p2):
        winner = board[3]
    elif board[6] == board[7] == board[8] == (p1) or board[6] == board[7] == board[8] == (p2):
        winner = board[6]
    elif board[0] == board[3] == board[6] == (p1) or board[0] == board[3] == board[6] == (p2):
        winner = board[0]
    elif board[1] == board[4] == board[7] == (p1) or board[1] == board[4] == board[7] == (p2):
        winner = board[1]
    elif board[2] == board[5] == board[8] == (p1) or board[2] == board[5] == board[8] == (p2):
        winner = board[2]
    elif board[0] == board[4] == board[8] == (p1) or board[0] == board[4] == board[8] == (p2):
        winner = board[0]
    elif board[2] == board[4] == board[6] == (p1) or board[2] == board[4] == board[6] == (p2):
        winner = board[2]
    elif board[0:] == (0, 9):
        print ('Tie Game')
    else:
        return False

    display_board(board)
    print(winner + " wins")
    return True


def start_game(p1, p2, board):
    nums_played = set()
    cur_input = ""
    while True:
        print("Current Board: ")
        display_board(board)
        while cur_input == "" or cur_input in nums_played or cur_input not in range(0, 9):
            cur_input = int(input('Select a number 0 through 8: '))
        nums_played.add(cur_input)
        board[cur_input] = p1
        if win_check(board):
            break
        if tie_check(board):
            break

        print("Current Board: ")
        display_board(board)
        while cur_input in nums_played or cur_input not in range(0, 9):
            cur_input = int(input('Select a number 0 through 8: '))
        nums_played.add(cur_input)
        board[cur_input] = p2
        if win_check(board):
            break
        if tie_check(board):
            break

    print("Game over")
    new_game(board)


def new_game(board):
    board = ['_']*9
    if win_check or tie_check:
        new = input("Would you like to play again (Y/N)?: ")
        if new == 'Y' or new == 'y':
            player_select()
            start_game(p1, p2, board)
        elif new == 'N' or new == 'n':
            print("Thanks come again!")
        else:
            return False


default_board = ['_']*9
p1, p2 = player_select()
start_game(p1, p2, default_board)
new_game(default_board)



