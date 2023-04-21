import os
import sys
import pygame
from button import Button
from Play import play

# Constants
WIDTH = 800
HEIGHT = 800
PLAY_BUTTON_WIDTH = 10
PLAY_BUTTON_HEIGHT =10

# Initialize Pygame
pygame.init()

# Set up the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers!")

# Load the assets
background = pygame.transform.scale(pygame.image.load(os.path.join('ASSETS', 'blue-technology-electronic-circuit-background_2846526.webp')), (WIDTH, HEIGHT))
play_image = pygame.transform.scale(pygame.image.load(os.path.join('ASSETS', 'Play Rect.png')), (PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT))

# Set up the fonts
menu_font = pygame.font.SysFont('comicsans', 100)

"""
This program is a game of Checkers.
It is written in Python and uses the Pygame library.
"""

import os
import sys
import pygame
from button import Button
from Play import play

def update_screen():
    """
    This function updates the screen with the background image.
    """
    WIN.blit(background, (0, 0))

def get_font(size):
    """
    This function returns the font 'Press-Start-2P' in the desired size.

    Parameters:
    size (int): The desired font size.

    Returns:
    font (pygame.font): The font object.
    """
    return pygame.font.SysFont('comicsans', size)

def main():
    """
    This is the main function of the program.
    It is responsible for displaying the main menu and handling user input.
    """
    while True:
        WIN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        CHEKERS = get_font(60).render("Welcome to Checkers", 1, "#b68f40")
        CHEKERS_RECT = CHEKERS.get_rect(center=(400, 200))
        WIN.blit(CHEKERS, CHEKERS_RECT)

        UNA = get_font(30).render("by Simeon Flamuraj", 1, (231,231,231))
        UNA_RECT = UNA.get_rect(center=(400, 280))
        WIN.blit(UNA, UNA_RECT)

        MENU_TEXT = get_font(50).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 430))

        PLAY_BUTTON = Button(image=None, pos=(400, 520),
                             text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color=(200,0,200))

        QUIT_BUTTON = Button(image=None, pos=(400, 600),
                             text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color=(200,100,100))

        WIN.blit(MENU_TEXT, MENU_RECT)


        for button in [PLAY_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()