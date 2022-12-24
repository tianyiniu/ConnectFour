from board import Board

if __name__ == "__main__":
    board = Board()
    board.print_board()
    while True:
        try:
            col = input("Enter col number: ")
            board.add_piece(piece="X", col=int(col))
            board.print_board()
        except Exception as e:
            print(e)
        