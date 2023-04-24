import pygame

def create_game_tree_visual():
    """
    This function creates a game tree visually in Pygame.
   
    """
    # Initialize Pygame
    pygame.init()
    
    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Set the background color
    background_color = (255, 255, 255)
    
    # Set the font
    font = pygame.font.SysFont('Arial', 30)
    
    # Set the text
    text = font.render('Game Tree', True, (0, 0, 0))
    
    # Set the position of the text
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    
    # Draw the text on the screen
    screen.fill(background_color)
    screen.blit(text, text_rect)
    pygame.display.update()
    
    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
