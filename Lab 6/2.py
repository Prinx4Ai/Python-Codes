import pygame
import sys

# Initialize Pygame
pygame.init()

# Window size
screen_width = 720
screen_height = 480

# Set up the screen and clock
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player Movement Example")
clock = pygame.time.Clock()

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Player settings
player_width, player_height = 100, 100
player_x, player_y = screen_width // 4, screen_height // 4
player_speed = 10

# Optional: Load player image (make sure the file exists!)
# Comment this out if you don't have an image file
# player_image = pygame.image.load('player.png')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player inside window bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width 
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # Fill screen with white
    screen.fill(white)

    # Draw player (rectangle)
    pygame.draw.rect(screen, black, (player_x, player_y, player_width, player_height))

    # OR draw player image instead of rectangle
    # screen.blit(player_image, (player_x, player_y))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # FPS limit

pygame.quit()
sys.exit()
