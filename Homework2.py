from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self._color = color   
        self._position = self._convert_to_indices(position)   
    
    def get_position(self):
        return self._convert_to_chess_notation(self._position)
    
    def set_position(self, new_position):
        self._position = self._convert_to_indices(new_position)
    
    def get_color(self):
        return self._color
    
    @abstractmethod
    def get_moves(self, board):
        pass
    
    def __str__(self):
        piece_symbols = {
            'King': {'white': '♔', 'black': '♚'},
            'Queen': {'white': '♕', 'black': '♛'},
            'Knight': {'white': '♘', 'black': '♞'}
        }
        return piece_symbols[self.__class__.__name__][self._color]
    
    def _convert_to_indices(self, chess_notation):
        column, row = chess_notation[0], chess_notation[1]
        return 8 - int(row), ord(column.lower()) - ord('a')
    
    def _convert_to_chess_notation(self, position):
        return chr(position[1] + ord('a')) + str(8 - position[0])

class King(Piece):
    def get_moves(self, board):
        row, col = self._position
        moves = [(row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
        return [self._convert_to_chess_notation((r, c)) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]

class Queen(Piece):
    def get_moves(self, board):
        row, col = self._position
        moves = []
        for i in range(8):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
            if i != 0:
                if 0 <= row + i < 8 and 0 <= col + i < 8:
                    moves.append((row + i, col + i))
                if 0 <= row - i < 8 and 0 <= col - i < 8:
                    moves.append((row - i, col - i))
                if 0 <= row + i < 8 and 0 <= col - i < 8:
                    moves.append((row + i, col - i))
                if 0 <= row - i < 8 and 0 <= col + i < 8:
                    moves.append((row - i, col + i))
        return [self._convert_to_chess_notation(move) for move in moves]

class Knight(Piece):
    def get_moves(self, board):
        row, col = self._position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [self._convert_to_chess_notation((r, c)) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]

class ChessSimple:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
    def add_piece(self, piece_class, position, color):
        piece = piece_class(color, position)
        row, col = piece._position
        if 0 <= row < 8 and 0 <= col < 8 and self.board[row][col] is None:
            self.board[row][col] = piece
        else:
            print("This position is invalid or occupied.")
    
    def remove_piece(self, position):
        row, col = self._convert_to_indices(position)
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
    
    def _convert_to_indices(self, chess_notation):
        column, row = chess_notation[0], chess_notation[1]
        return 8 - int(row), ord(column.lower()) - ord('a')


#usage
game = ChessSimple()
game.add_piece(King, "e8", "white")
game.add_piece(Queen, "d1", "black")
game.add_piece(Knight, "e4", "white")

game.display_board()
print("possible moves for the King ♔ are:", game.board[0][4].get_moves(game.board))
print("possible moves for the Queen ♛ are:", game.board[7][3].get_moves(game.board))
print("possible moves for the Knight ♘ are:", game.board[4][4].get_moves(game.board))
 