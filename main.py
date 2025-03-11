import pygame
from player import Player

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
BACKGROUND_COLOR = (75, 0, 130)  # purple

# Set up the game window and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

# Create the player
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

# MAIN LOOP
running = True
while running:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game objects
    player.update()
    
    # Render everything
    screen.fill(BACKGROUND_COLOR)
    player.draw(screen)
    
    # Update the display
    pygame.display.flip()
    
    # 60 FPS
    clock.tick(60)

pygame.quit()