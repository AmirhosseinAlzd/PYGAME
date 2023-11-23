import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
WORD_LIST = ["PYTHON", "ZAHRA", "DONYA", "SAJI", "APPLE"]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Choose a random word
word_to_guess = random.choice(WORD_LIST)
guessed_letters = set()

# Initialize variables
incorrect_guesses = 0
game_over = False

# Function to draw the word with underscores and guessed letters
def draw_word():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    font = pygame.font.Font(None, FONT_SIZE)
    text = font.render(display_word, True, BLACK)
    screen.blit(text, (20, HEIGHT - 100))

# Function to draw the hangman figure
def draw_hangman(incorrect_guesses):
    font = pygame.font.Font(None, 48)
    text = font.render(f"Incorrect Guesses: {incorrect_guesses}", True, BLACK)
    screen.blit(text, (20, 20))

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key >= 97 and event.key <= 122:  # Check if a lowercase letter key is pressed
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in word_to_guess:
                        incorrect_guesses += 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw hangman figure
    draw_hangman(incorrect_guesses)

    # Draw word
    draw_word()

    pygame.display.update()

    # Check for win or loss
    if set(word_to_guess) == guessed_letters:
        font = pygame.font.Font(None, 72)
        text = font.render("You Win!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause for a few seconds before exiting
        game_over = True
    elif incorrect_guesses >= 7:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Pause for a few seconds before exiting
        game_over = True

pygame.quit()
sys.exit()
 