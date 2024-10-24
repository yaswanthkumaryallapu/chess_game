import chess

# Function to display the current state of the board
def print_board(board):
    print(board)

# Function to get player's input and check if the move is valid
def get_player_move(board):
    while True:
        move_input = input("Enter your move (e.g., e2e4): ").strip()
        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move! Please enter a legal move.")
        except ValueError:
            print("Invalid move format! Use UCI format like 'e2e4'.")

# Main game loop
def play_game():
    board = chess.Board()  # Initialize an empty board
    print("Welcome to Text-Based Chess!")
    print_board(board)     # Display the starting board

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print("White's turn")
        else:
            print("Black's turn")

        # Get the player's move
        move = get_player_move(board)
        board.push(move)  # Apply the move to the board
        print_board(board)  # Print the updated board

        # Check for game end conditions
        if board.is_checkmate():
            print("Checkmate!")
            winner = "White" if board.turn == chess.BLACK else "Black"
            print(f"{winner} wins!")
            break  # Exit the loop since the game is over
        elif board.is_stalemate():
            print("Stalemate!")
            break  # Exit the loop since the game is over
        elif board.is_insufficient_material():
            print("Draw due to insufficient material.")
            break  # Exit the loop since the game is over
        elif board.is_seventyfive_moves():
            print("Draw due to 75-move rule.")
            break  # Exit the loop since the game is over
        elif board.is_fivefold_repetition():
            print("Draw due to fivefold repetition.")
            break  # Exit the loop since the game is over
        elif board.is_variant_draw():
            print("Draw.")
            break  # Exit the loop since the game is over

# Run the game
if __name__ == "__main__":
    play_game()
