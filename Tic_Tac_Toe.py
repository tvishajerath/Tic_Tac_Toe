import numpy as np
import random
    

# creating the tic tac toe board by initializing a 3x3 array with default type as integers and default value as 0
def create_board():
    return np.zeros((3,3),dtype=int)

# displaying tic tac toe board
def display_board(board):
    symbols = {0: " ", 1: "X", 2: "O"}
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * 9)

#returns the empty spaces in the board where a play can be made
def empty_board_spaces(board):
    return [(i,j) for i in range(3) for j in range(3) if board[i][j]==0]

# chooses a random empty place to add the AI move out of the possible board spaces
def random_place(board, player):
    loc = random.choice(empty_board_spaces(board))
    board[loc[0]][loc[1]] = player
    
    return board

#executes the player's move
def player_move(board, player):
    while True:
        try:
            row_move = int(input("Enter which row you want to play in (1, 2, or 3): "))
            col_move = int(input("Enter which column you want to play in (1, 2, or 3): "))

            if row_move not in [1, 2, 3] or col_move not in [1, 2, 3]:
                print("Row and column must be 1, 2, or 3.")
                continue #goes back to the top of the while True loop

            row = row_move - 1
            col = col_move - 1

            if board[row][col] == 0:
                board[row][col] = player
                break
            else:
                print("Cell is already taken. Try a different move.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

#returns true if a row is made
def row_win(board, player):
    return np.any(np.all(board == player, axis=1))

#returns true if a column is made
def col_win(board, player):
    return np.any(np.all(board == player, axis=0))

#returns true if a diagional is made
def diag_win(board, player):
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)

#evaluates the result of the game
def evaluate(board):
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

#executes the game
def play_game(mode):
    board = create_board()
    winner = 0
    move_count = 1

    display_board(board)

    while winner == 0:
        if mode == 1:
            # Player vs AI
            player_move(board, 1)
            display_board(board)
            winner = evaluate(board)
            if winner != 0:
                break
            print("AI is making a move...")
            board = random_place(board, 2)
        else:
            # 2 Player
            current_player = 1 if move_count % 2 == 1 else 2
            player_move(board, current_player)

        move_count += 1
        display_board(board)
        winner = evaluate(board)

    if winner == -1:
        print("It's a draw!")
    else:
        print(f"Player {winner} wins!")

while True:
    choice = input("Choose game mode:\n1 - Play vs AI\n2 - 2 Player\nEnter 1 or 2: ").strip()
    if choice in ['1', '2']:
        play_game(int(choice))
        break
    else:
        print("Invalid choice. Try again.")
