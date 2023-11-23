import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 720, 720
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_WIDTH = 10
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Initialize the game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

current_player = 'X'
winner = None
game_over = False

# Function to draw the game board
def draw_board():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Function to handle player clicks
def handle_click(row, col):
    global current_player, game_over

    if board[row][col] == '' and not game_over:
        board[row][col] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Function to check for a win
def check_win():
    global winner, game_over

    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            game_over = True
            return

    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            game_over = True
            return

    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        game_over = True
        return

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            handle_click(row, col)
            check_win()

    screen.fill(BG_COLOR)
    draw_board()

    # Draw X and O
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                x_center, y_center = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 3
                pygame.draw.line(screen, LINE_COLOR, (x_center - radius, y_center - radius),
                                 (x_center + radius, y_center + radius), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, (x_center + radius, y_center - radius),
                                 (x_center - radius, y_center + radius), LINE_WIDTH)
            elif board[row][col] == 'O':
                x_center, y_center = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 3
                pygame.draw.circle(screen, LINE_COLOR, (x_center, y_center), radius, LINE_WIDTH)

    # Display the winner
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.update()
