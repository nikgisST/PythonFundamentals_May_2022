matrix = [[1,2,3,4,5], [6,7,8,9,10]]

print(matrix[0][3])
#4

print('\n'.join(str(s) for s in matrix))
print(matrix[0][1])

# Tic-Tac-Toe

# Display the board
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

# Check for a win
def check_win(board, player):
    return (
        (board[7] == board[8] == board[9] == player) or  # top row
        (board[4] == board[5] == board[6] == player) or  # middle row
        (board[1] == board[2] == board[3] == player) or  # bottom row
        (board[7] == board[4] == board[1] == player) or  # left column
        (board[8] == board[5] == board[2] == player) or  # middle column
        (board[9] == board[6] == board[3] == player) or  # right column
        (board[7] == board[5] == board[3] == player) or  # diagonal
        (board[9] == board[5] == board[1] == player)     # diagonal
    )

# Check for a tie
def check_tie(board):
    return ' ' not in board[1:]

# Play the game
def play_game():
    board = [' '] * 10
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        move = int(input('Enter your move (1-9): '))

        if board[move] == ' ':
            board[move] = current_player
            if check_win(board, current_player):
                display_board(board)
                print('Congratulations! Player', current_player, 'wins!')
                game_over = True
            elif check_tie(board):
                display_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('That move is not valid. Try again.')

play_game()
