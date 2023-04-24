# Import necessary libraries
import pygame
import os
from game import Game
from MinMax_Algorithm import MiniMAx
from Options import hardness

# Set constants
WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = WIDTH // 8
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
background = pygame.transform.scale(
    pygame.image.load(os.path.join('ASSETS', 'blue-technology-electronic-circuit-background_2846526.webp')),
    (WIDTH, HEIGHT))

# Function to get font
def get_font(size):
    """
    This function is used to get the font of the game.


    Returns:
    pygame.font.SysFont: The font of the game.
    """
    return pygame.font.SysFont('comicsans', size)

# Function to get mouse position
def get_mouse(pos):
    """
    This function is used to get the mouse position.


    Returns:
    row (int): The row of the mouse.
    col (int): The column of the mouse.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main function to play the game
def play():
    """
    This function is used to play the game.
    """
    # Get the hardness of the game
    hard = hardness()
    turn = hardness()
    game = Game(WIN, turn)

    # Main game loop
    while True:
        # AI turn
        if game.turn == WHITE:
            value, new_board = MiniMAx(game.get_board(), hard, turn, game)


            game.AI_move(new_board)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                from main import  main
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse(pos)
                game.select(row, col)

        # Update the game
        game.update()

# Main function to run the game
if __name__ == "__main__":
    play()
