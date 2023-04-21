import pygame
import os

# Define colors
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREY=(128,128,128)

# Define window size
WIDTH = 800

# Define rows and columns
ROWS, COLS = 8, 8

# Calculate square size
SQUARE_SIZE=WIDTH//COLS

# Load crown image
CROWN=pygame.transform.scale(pygame.image.load(os.path.join('ASSETS', 'crown.png')),(44,25))

class piece():
    """
    This class represents a piece in a game.
    """
    def __init__(self,row,col,color):
        """
        Constructor for the piece class.
        :param row: The row of the piece.
        :param col: The column of the piece.
        :param color: The color of the piece.
        """
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x=0
        self.y=0
        self.pos()


    def move(self,row,col):
        """
        Move the piece to a new row and column.
        :param row: The new row of the piece.
        :param col: The new column of the piece.
        """
        self.row=row
        self.col=col
        self.pos()

    def pos(self):
        """
        Calculate the x and y coordinates of the piece.
        """
        self.x=SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y=SQUARE_SIZE*self.row+SQUARE_SIZE//2

    def M_king(self):
        """
        Make the piece a king.
        """
        self.king = True

    def draw(self,win):
        """
        Draw the piece on the window.
        :param win: The window to draw the piece on.
        """
        radius= SQUARE_SIZE//2-15
        pygame.draw.circle(win,GREY,(self.x,self.y),radius)
        pygame.draw.circle(win,self.color,(self.x,self.y),radius+2)
        if self.king:
            win.blit(CROWN,(self.x-CROWN.get_width()//2,self.y-CROWN.get_height()//2))

    def __repr__(self):
        """
        Represent the piece as a string.
        :return: The color of the piece as a string.
        """
        return str(self.color)