import numpy as np
import random

# Creates an empty 3x3 board filled with zeros
def create_board():
    return np.zeros((3, 3), dtype=int)

# Prints the board with X for Player 1, O for Player 2, and spaces for empty cells
def display_board(board):
    symbols = {0: " ", 1: "X", 2: "O"}
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * 9)

# Returns a list of empty positions on the board
def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

# Chooses a random empty cell and places the player's symbol there
def random_place(board, player):
    loc = random.choice(possibilities(board))
    board[loc] = player
    return board

# Smart AI: tries to win, then block, else plays randomly
def smart_place(board, ai_player):
    human = 1 if ai_player == 2 else 2  # identify the human player

    # Check if AI can win in one move
    for move in possibilities(board):
        temp_board = board.copy()
        temp_board[move] = ai_player
        if evaluate(temp_board) == ai_player:
            board[move] = ai_player
            return board

    # Check if human can win in one move → block them
    for move in possibilities(board):
        temp_board = board.copy()
        temp_board[move] = human
        if evaluate(temp_board) == human:
            board[move] = ai_player
            return board

    # Else play a random move
    return random_place(board, ai_player)

# Handles user input and safely places their move
def player_move(board, player):
    while True:
        try:
            row_move = int(input("Enter which row you want to play in (1, 2, or 3): "))
            col_move = int(input("Enter which column you want to play in (1, 2, or 3): "))

            # Check if input is in valid range
            if row_move not in [1, 2, 3] or col_move not in [1, 2, 3]:
                print("Row and column must be 1, 2, or 3.")
                continue

            row = row_move - 1
            col = col_move - 1

            # Check if the selected cell is empty
            if board[row][col] == 0:
                board[row][col] = player
                break
            else:
                print("Cell is already taken. Try a different move.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Checks if the player has won in any row
def row_win(board, player):
    return np.any(np.all(board == player, axis=1))

# Checks if the player has won in any column
def col_win(board, player):
    return np.any(np.all(board == player, axis=0))

# Checks if the player has won in a diagonal
def diag_win(board, player):
    return np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player)

# Evaluates the current board state:
# returns 1 or 2 if a player has won,
# -1 if it's a draw,
# 0 if the game is still ongoing
def evaluate(board):
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

# Main game loop
def play_game(mode):
    board = create_board()
    winner = 0  # 0 means game is ongoing
    move_count = 1  # used to switch turns in 2-player mode

    display_board(board)

    while winner == 0:
        if mode == 1:
            # Player vs AI mode
            player_move(board, 1)  # Player 1 (human) moves
            display_board(board)
            winner = evaluate(board)
            if winner != 0:
                break
            print("AI is making a move...")
            board = smart_place(board, 2)  # AI (Player 2) uses smart logic
        else:
            # 2 Player mode
            current_player = 1 if move_count % 2 == 1 else 2
            player_move(board, current_player)

        move_count += 1
        display_board(board)
        winner = evaluate(board)

    # Game ended: show result
    if winner == -1:
        print("It's a draw!")
    else:
        print(f"Player {winner} wins!")

# Prompt user to choose the game mode
while True:
    choice = input("Choose game mode:\n1 - Play vs AI\n2 - 2 Player\nEnter 1 or 2: ").strip()
    if choice in ['1', '2']:
        play_game(int(choice))
        break
    else:
        print("Invalid choice. Try again.")
