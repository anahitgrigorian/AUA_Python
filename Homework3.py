import random
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
        return [
            self._convert_to_chess_notation((r, c))
            for r, c in moves
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] is None or board[r][c].get_color() != self._color)
        ]

class Queen(Piece):
    def get_moves(self, board):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        moves = []
        for d in directions:
            r, c = self._position
            while True:
                r += d[0]
                c += d[1]
                if 0 <= r < 8 and 0 <= c < 8:
                    if board[r][c] is None:
                        moves.append(self._convert_to_chess_notation((r, c)))
                    elif board[r][c].get_color() != self._color:
                        moves.append(self._convert_to_chess_notation((r, c)))
                        break
                    else:
                        break
                else:
                    break
        return moves


class Knight(Piece):
    def get_moves(self, board):
        row, col = self._position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        return [
            self._convert_to_chess_notation((r, c))
            for r, c in moves
            if 0 <= r < 8 and 0 <= c < 8 and (board[r][c] is None or board[r][c].get_color() != self._color)
        ]

 
class ChessGame:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.pieces = {"white": [], "black": []}
        self.current_turn = random.choice(["white", "black"])
        self._setup_pieces()
    
    def _setup_pieces(self):
        piece_types = [King, Queen, Knight]
        for color in ["white", "black"]:
            for _ in range(random.randint(1, 4)):
                piece_class = random.choice(piece_types)
                while True:
                    position = chr(random.randint(97, 104)) + str(random.randint(1, 8))
                    row, col = self._convert_to_indices(position)
                    if self.board[row][col] is None:
                        piece = piece_class(color, position)
                        self.board[row][col] = piece
                        self.pieces[color].append(piece)
                        break
    
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
    
    def play_game(self):
        while all(self.pieces.values()):
            self.display_board()
            print(f"{self.current_turn.capitalize()} to move.")
            piece_position = input("Enter piece position (or 'q' to quit): ").lower()
            if piece_position == 'q':
                break
            
            if piece_position not in [p.get_position() for p in self.pieces[self.current_turn]]:
                print("Invalid selection. Please choose one of your pieces.")
                continue
            
            row, col = self._convert_to_indices(piece_position)
            piece = self.board[row][col]
            moves = piece.get_moves(self.board)
            print("Available moves:", moves)
            
            move = input("Choose move (or 'c' to cancel): ").lower()
            if move in moves:
                new_row, new_col = self._convert_to_indices(move)
                if self.board[new_row][new_col] is not None:
                    captured_piece = self.board[new_row][new_col]
                    self.pieces[captured_piece.get_color()].remove(captured_piece)
                
                self.board[row][col] = None
                piece.set_position(move)
                self.board[new_row][new_col] = piece
                self.current_turn = "white" if self.current_turn == "black" else "black"
            elif move == 'c':
                continue
            else:
                print("Invalid move.")
        
        winner = "White" if self.pieces["black"] == [] else "Black"
        print(f"Game Over! {winner} wins!")
    
    def _convert_to_indices(self, chess_notation):
        column, row = chess_notation[0], chess_notation[1]
        return 8 - int(row), ord(column.lower()) - ord('a')

#USAGE
game = ChessGame()
game.play_game()
