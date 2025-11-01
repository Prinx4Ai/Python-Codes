import pygame
import random
import sys

pygame.init()

# Screen setup
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Falling Blocks")
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Player properties
player_width, player_height = 100, 20
player_x = width // 2 - player_width // 2
player_y = height - player_height - 10
player_speed = 10

# Falling block properties
block_size = 20
block_x = random.randint(0, width - block_size)
block_y = 0
block_speed = 7

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Move block down
    block_y += block_speed

    # Check if block caught
    if (block_y + block_size >= player_y) and (player_x < block_x + block_size) and (player_x + player_width > block_x):
        score += 1
        block_x = random.randint(0, width - block_size)
        block_y = 0

    # Reset block if it falls past bottom
    if block_y > height:
        block_x = random.randint(0, width - block_size)
        block_y = 0

    # Draw player
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    # Draw block
    pygame.draw.rect(screen, red, (block_x, block_y, block_size, block_size))

    # Draw score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
