from helper import *
from custom_errors import *

class Board:
    """Represents connect four grid and handles player and game actions."""
    # Initialize board
    def __init__(self) -> None:
        self.board = [["_" for _ in range(7)] for _ in range(6)]

    # Print board
    def print_board(self) -> None:
        """Formats and prints the current board."""
        for row in self.board:
            print("| " + " | ".join(row) + " |")
        print("-"*29)
        col_labels = lst_int_to_str([1, 2, 3, 4, 5, 6, 7])
        col_labels = "| " + " | ".join(col_labels) + " |"
        print("".join(col_labels))
        print("-"*29)

    # Return board
    def get_board(self) -> list[list[str]]:
        """Returns the current board in play."""
        return self.board

    # Add piece
    def add_piece(self, piece: str, col: int):
        "Adds a piece into a 1-indexed column (1-7) if a spot available."
        if col < 1 or col > 7:
            msg = "Ioutofrange"
            raise ColumnIndexOutOfRangeError(col=col, msg=msg)
        col -= 1 # Converts column index to 0-indexed
        for i in range(5, -1, -1):
            if self.board[i][col] == "_":
                self.board[i][col] = piece
                return
        else:
            raise ColumnFullError(col=col+1, msg="Column already full.")

    # Detect whether a player has won
    def has_won(self, piece:str) -> str:
        """Determines if a player has four connected pieces. Returns 'X', 'O' or None is no winner."""
        if piece != "X" or piece != "O":
            raise PieceDoesNotExistError(piece, "Piece does not exist")
        win_str = piece*5
        # Each each row for win
        for row in self.board:
            row_str = "".join(row)
            if win_str in row_str:
                return True
        for i in range(0, 6):
            col_str = ""
            for row in self.board:
                col_str += row[i]

