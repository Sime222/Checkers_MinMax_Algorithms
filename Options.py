import os

"""
This program is used to set the difficulty and starting player of a game.
"""

from button import Button
import pygame

# Set the window size
WIDTH = 800
HEIGHT = 800

# Set the colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Initialize pygame
pygame.init()

# Create the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the background image
background = pygame.transform.scale(
    pygame.image.load(os.path.join('ASSETS', 'blue-technology-electronic-circuit-background_2846526.webp')),
    (WIDTH, HEIGHT))


def get_font(size):
    """
    This function returns the Press-Start-2P font in the desired size.


    Returns:
    pygame.font.SysFont: The font object.
    """

    return pygame.font.SysFont('comicsans', size)


def hardness():
    """
    This function is used to set the difficulty and starting player of the game.
    """

    while True:

        # Draw the background
        WIN.blit(background, (0, 0))

        # Get the mouse position
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Draw the difficulty text
        difficilty = get_font(40).render("Difficilty:", 1, GRAY)
        difficilty_RECT = difficilty.get_rect(center=(400, 300))
        WIN.blit(difficilty, difficilty_RECT)

        # Draw the easy button
        OPTIONS_EASY = Button(image=None, pos=(200, 380),
                              text_input="EASY", font=get_font(30), base_color=(255, 255, 255),
                              hovering_color="Green")

        OPTIONS_EASY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_EASY.update(WIN)

        # Draw the medium button
        OPTIONS_MEDIUM = Button(image=None, pos=(400, 380),
                                text_input="MEDIUM", font=get_font(30), base_color=(255, 255, 255),
                                hovering_color="Green")

        OPTIONS_MEDIUM.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MEDIUM.update(WIN)

        # Draw the hard button
        OPTIONS_HARD = Button(image=None, pos=(600, 380),
                              text_input="HARD", font=get_font(30), base_color=(255, 255, 255),
                              hovering_color="Green")

        OPTIONS_HARD.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_HARD.update(WIN)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                from main import main
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_EASY.checkForInput(pygame.mouse.get_pos()):
                    difficulty_level = 1

                    return difficulty_level
                elif OPTIONS_HARD.checkForInput(pygame.mouse.get_pos()):
                    difficulty_level =  3
                    return difficulty_level
                elif OPTIONS_MEDIUM.checkForInput(pygame.mouse.get_pos()):
                    difficulty_level = 2
                    return difficulty_level

        CHOOSE = get_font(40).render("Choose who starts the game:", 1, GRAY)
        CHOOSE_RECT = CHOOSE.get_rect(center=(400, 450))
        WIN.blit(CHOOSE, CHOOSE_RECT)


        OPTIONS_AI_PLAYER = Button(image=None, pos=(300, 520),
                                   text_input="AI_player", font=get_font(30), base_color=(255, 255, 255),
                                   hovering_color="Green")

        OPTIONS_AI_PLAYER.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_AI_PLAYER.update(WIN)

        OPTIONS_PLAYER = Button(image=None, pos=(500, 520),
                                text_input="Player ", font=get_font(30), base_color=(255, 255, 255),
                                hovering_color="Green")

        OPTIONS_PLAYER.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_PLAYER.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                from main import main
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_AI_PLAYER.checkForInput(pygame.mouse.get_pos()):
                    starting_player = WHITE
                    return starting_player
                elif OPTIONS_PLAYER.checkForInput(pygame.mouse.get_pos()):
                    starting_player = RED
                    return starting_player

        pygame.display.update()




