import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake = [(5, 5)]
snake_direction = (1, 0)

# Food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)

    new_head = ((snake[0][0] + snake_direction[0]) % GRID_WIDTH, (snake[0][1] + snake_direction[1]) % GRID_HEIGHT)

    if new_head == food:
        snake.insert(0, food)
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.insert(0, new_head)
        snake.pop()

    if len(snake) > 1 and new_head in snake[1:]:
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw food
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

# Game over
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, GREEN)
screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
pygame.display.update()

pygame.time.delay(2000)  # Pause for a few seconds before exiting
pygame.quit()
sys.exit()
