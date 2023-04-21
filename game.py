import pygame
from Board import Board, get_font

RED=(255,0,0)
WHITE=(255,255,255)
BLUE=(0,100,255)
WIN_C=(0,100,200)
ROWS, COLS =8 ,8
WIDTH = 800
HEIGHT = 800
SQUARE_SIZE=WIDTH//COLS


class Game:
    """
    This class is responsible for the game logic and drawing the game board.
    """

    def __init__(self,win,starting_player):
        """
        Initializes the game.

        Parameters:
            win (pygame.Surface): The game window.
            starting_player (tuple): The starting player's color.
        """
        self.selected = None
        self.board = Board()
        self.turn = starting_player
        self.valid_moves = {}
        self.win = win

    def update(self):
        """
        Updates the game board.
        """
        self.board.draw(self.win)
        self.draw_moves(self.valid_moves)

        if self.winner()!=None:
            self.draw_winner()

        pygame.display.update()


    def reset(self):
        """
        Resets the game.
        """
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves={}

    def winner(self):
        """
        Checks if there is a winner.

        Returns:
            int: The winner's color.
        """
        return self.board.winner()

    def select(self,row,col):
        """
        Selects a piece on the board.

        Parameters:
            row (int): The row of the piece.
            col (int): The column of the piece.

        Returns:
            bool: True if the piece was selected, False otherwise.
        """
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)

        piece = self.board.get_piece(row,col)
        if piece !=0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves=self.board.get_valid_moves(piece)
            return True
        return False

    def _move(self, row, col):
        """
        Moves a piece on the board.

        Parameters:
            row (int): The row of the piece.
            col (int): The column of the piece.

        Returns:
            bool: True if the piece was moved, False otherwise.
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.next_turn()
        else:
            return False

        return True





    def next_turn(self):
        """
        Switches turns.
        """
        self.valid_moves={}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def draw_moves(self, moves):
        """
        Draws the valid moves on the board.

        Parameters:
            moves (dict): The valid moves.
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)


    def draw_winner(self):
        """
        Draws the winner on the board.
        """
        winner = self.winner()

        if self.winner() != None:
            if winner == 1:
                mess="white won"
            elif winner == -1:
                mess="red won"

            UNA = get_font(100).render(mess, 1, WIN_C)
            UNA_RECT = UNA.get_rect(center=(400, 400))
            self.win.blit(UNA, UNA_RECT)





    #lidhje me ai
    def get_board(self):
        """
        Gets the game board.

        Returns:
            Board: The game board.
        """
        return  self.board

    def AI_move(self,board):
        """
        Makes a move for the AI.

        Parameters:
            board (Board): The game board.
        """
        self.board = board
        self.next_turn()