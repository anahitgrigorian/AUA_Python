class Piece:
    def __init__(self, color, position):
        self.color = color  #it can be either white or black
        self.position = position  #this is for the position (row and column)
    
    def get_moves(self):
        """Returns a list of possible moves for the piece."""
        pass

    def __str__(self):
        piece_symbols = {
            'King': {'white': '♔', 'black': '♚'},
            'Queen': {'white': '♕', 'black': '♛'},
            'Knight': {'white': '♘', 'black': '♞'}
        }
        return piece_symbols[self.__class__.__name__][self.color]


class King(Piece):
    def get_moves(self):
        row, col = self.position
        moves = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]


class Queen(Piece):
    def get_moves(self):
        row, col = self.position
        moves = []
        for i in range(8):
            if i != row:
                moves.append((i, col))  #this is for vertical moves
            if i != col:
                moves.append((row, i))  #this is for horizontal moves
            if i != 0:
                if 0 <= row + i < 8 and 0 <= col + i < 8:
                    moves.append((row + i, col + i))  #diagonal down/right
                if 0 <= row - i < 8 and 0 <= col - i < 8:
                    moves.append((row - i, col - i))  #diagonal up/left
                if 0 <= row + i < 8 and 0 <= col - i < 8:
                    moves.append((row + i, col - i))  #diagonal down/left
                if 0 <= row - i < 8 and 0 <= col + i < 8:
                    moves.append((row - i, col + i))  #diagonal up/right
        return moves


class Knight(Piece):
    def get_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]


class ChessSimple:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
    def add_piece(self, piece, position):
        row, col = position
        if 0 <= row < 8 and 0 <= col < 8 and self.board[row][col] is None:
            self.board[row][col] = piece
            piece.position = position
        else:
            print("This position is invalid or occupied.")
    
    def remove_piece(self, position):
        row, col = position
        if 0 <= row < 8 and 0 <= col < 8 and self.board[row][col] is not None:
            self.board[row][col] = None
        else:
            print("No piece at this position.")
    
    def display_board(self):
        print("  a  b  c  d  e  f  g  h")
        print("  -----------------------")
        for i, row in enumerate(self.board):
            row_display = f"{8 - i} |"
            for piece in row:
                row_display += f" {str(piece)} " if piece else " . "
            row_display += f"| {8 - i}"
            print(row_display)
        print("  -----------------------")
        print("  a  b  c  d  e  f  g  h\n")




#example
game = ChessSimple()
king = King("white", (0, 4))
queen = Queen("black", (7, 3))
knight = Knight("white", (4, 4))

game.add_piece(king, (0, 4))
game.add_piece(queen, (7, 3))
game.add_piece(knight, (4, 4))

game.display_board()


