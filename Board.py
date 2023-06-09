# Import necessary libraries
import pygame
from pieces import piece

# Set constants
WIDTH = 800
HEIGHT = 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Function to get font
def get_font(size):
    """
    Returns Press-Start-2P in the desired size
    :return: font object
    """
    return pygame.font.SysFont('comicsans', size)


class Board:
    """
    Class to represent the board
    """
    def __init__(self):
        """
        Initialize the board
        """
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        """
        Draws the squares on the board
        """
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, (200, 200, 200), (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        Creates the board
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def move(self, piece, row, col):
        """
        Move the piece to the given row and column
       
        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.M_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        """
        Get the piece at the given row and column
      
        """
        return self.board[row][col]

    def draw(self, win):
        """
        Draw the board
        
        """
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def _traverse_left(self, row, end_row, step, color, left):
        """
        Helper function to traverse left
      
        :return: dictionary of valid moves
        """
        moves = {}
        while row != end_row:
            if left >= 0 and self.board[row][left] == 0:
                moves[(row, left)] = None
            elif left >= 0 and self.board[row][left].color != color:
                moves[(row, left)] = (row + step, left - 1)
            row += step
            left -= 1
        return moves

    def _traverse_right(self, row, end_row, step, color, right):
        """
        Helper function to traverse right
     
        :return: dictionary of valid moves
        """
        moves = {}
        while row != end_row:
            if right < COLS and self.board[row][right] == 0:
                moves[(row, right)] = None
            elif right < COLS and self.board[row][right].color != color:
                moves[(row, right)] = (row + step, right + 1)
            row += step
            right += 1
        return moves

    def get_valid_moves(self, piece):
        """
        Get the valid moves for the given piece
        
        :return: dictionary of valid moves
        """
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    

    def remove(self, pieces):
        """
        Removes pieces from the board.

        """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        """Checks if there is a winner.

        Returns:
            int: 1 if red won, -1 if white won, None if no winner.
        """
        if self.red_left <= 0:
            return 1
        elif self.white_left <= 0:
            return -1
        return None

    # score of board
    def eval(self):
        """Evaluates the board.

        Returns:
            float: The score of the board.
        """
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        """Gets all pieces of a certain color.

        Returns:
            list: A list of pieces of the specified color.
        """
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
