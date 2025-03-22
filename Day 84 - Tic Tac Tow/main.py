# Initialize the board

import random


class TicTacToe:
    def __init__(self):
        # Initialize the board with empty spaces
        self.board = [
            ["   ", "   ", "   "],
            ["   ", "   ", "   "],
            ["   ", "   ", "   "],
        ]
        self.game_over = False
        self.winner = None
        self.player = random.choice(["X", "O"])

    def print_board(self):
        for idx, row in enumerate(self.board):
            print("|".join(row))
            if idx < 2:
                print("-" * 11)

    def make_move(self, row, col):
        if self.board[row][col] == "   ":
            self.board[row][col] = f" {self.player} "
            self.check_winner(row, col)
        else:
            print("Invalid move. Try again.")

    def check_winner(self, row, col):
        # Check row
        if all((self.board[row][c].strip()) == self.player for c in range(3)):
            self.game_over = True
            self.winner = self.player
            print(f"Player {self.player} wins!")
            return

        # Check column
        if all(self.board[r][col].strip() == self.player for r in range(3)):
            self.game_over = True
            self.winner = self.player
            print(f"Player {self.player} wins!")
            return

        # Check diagonals
        if row == col and all(
            self.board[i][i].strip() == self.player for i in range(3)
        ):
            self.game_over = True
            self.winner = self.player
            print(f"Player {self.player} wins!")
            return

        if row + col == 2 and all(
            self.board[i][2 - i].strip() == self.player for i in range(3)
        ):
            self.game_over = True
            self.winner = self.player
            print(f"Player {self.player} wins!")
            return

        # Check for draw
        if all(self.board[r][c] != "   " for r in range(3) for c in range(3)):
            self.game_over = True
            print("It's a draw!")


if __name__ == "__main__":
    # Example usage
    game = TicTacToe()
    game.print_board()
    while not game.game_over:
        # Get user input
        print(f"Player {game.player}'s turn")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if game.board[row][col] == "   ":
            game.make_move(row, col)
            game.print_board()
            # Switch player
            if not game.game_over:
                game.player = "O" if game.player == "X" else "X"
        else:
            print("Invalid move. Try again.")
