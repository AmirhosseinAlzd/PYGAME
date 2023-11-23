import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ENEMY_SIZE = 30
ENEMY_SPEED = 3
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Enemies
enemies = [pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)]

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_SPEED > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x + PLAYER_SPEED + PLAYER_SIZE < WIDTH:
        player.x += PLAYER_SPEED

    # Move enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
            score += 1

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw player and enemies
    pygame.draw.rect(screen, RED, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(30)

# Game over
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, RED)
screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
pygame.display.update()

pygame.time.delay(2000)  # Pause for a few seconds before exiting
pygame.quit()
