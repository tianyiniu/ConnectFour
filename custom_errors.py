class ColumnIndexOutOfRangeError(Exception):
    def __init__(self, col:int, msg:str):
        self.col = col
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self) -> str:
        return f"Column index {self.col} out of range. Must be 1-7"


class ColumnFullError(Exception):
    def __init__(self, col:int, msg: str):
        self.col = col
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self) -> str:
        return f"Column {self.col} is already full."


class PieceDoesNotExistError(Exception):
    def __init__(self, piece:int, msg: str):
        self.piece = piece
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self) -> str:
        return f"Piece {self.piece} does not exist."