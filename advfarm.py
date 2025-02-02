import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farming Simulation")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)       # Planted crop
BROWN = (139, 69, 19)     # Empty soil
BLUE = (0, 0, 255)        # Watered crop
YELLOW = (255, 255, 0)    # Fully grown crop
BLACK = (0, 0, 0)         # Grid lines
RED = (255, 0, 0)         # Out of coins warning

# Grid dimensions
GRID_ROWS, GRID_COLS = 5, 6
CELL_SIZE = 80
GRID_START_X, GRID_START_Y = 100, 100

# Crop states
EMPTY = 0
PLANTED = 1
GROWING = 2
GROWN = 3

# Game variables
coins = 50
plant_cost = 5
harvest_reward = 10

# Initialize the farm grid (2D array)
grid = [[EMPTY for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
growth_timers = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]  # Timer for crop growth

# Font for displaying coins
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = GRID_START_X + col * CELL_SIZE
            y = GRID_START_Y + row * CELL_SIZE
            
            # Draw cell background based on crop state
            if grid[row][col] == EMPTY:
                pygame.draw.rect(screen, BROWN, (x, y, CELL_SIZE, CELL_SIZE))  # Empty soil
            elif grid[row][col] == PLANTED:
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))  # Planted crop
            elif grid[row][col] == GROWING:
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))  # Watered crop
            elif grid[row][col] == GROWN:
                pygame.draw.rect(screen, YELLOW, (x, y, CELL_SIZE, CELL_SIZE))  # Fully grown crop

            # Draw grid lines
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)

# Function to get the grid position from mouse coordinates
def get_grid_position(mouse_x, mouse_y):
    col = (mouse_x - GRID_START_X) // CELL_SIZE
    row = (mouse_y - GRID_START_Y) // CELL_SIZE
    if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
        return row, col
    return None

# Function to display coins
def display_coins():
    coin_text = font.render(f"Coins: {coins}", True, BLACK)
    screen.blit(coin_text, (10, 10))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_grid()
    display_coins()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grid_pos = get_grid_position(pos[0], pos[1])
            if grid_pos:
                row, col = grid_pos
                if grid[row][col] == EMPTY and coins >= plant_cost:  # Plant crop
                    grid[row][col] = PLANTED
                    coins -= plant_cost
                    growth_timers[row][col] = time.time() + 5  # 5 seconds to grow
                    # Uncomment when sound files are available:
                    # plant_sound.play()

                elif grid[row][col] == GROWN:  # Harvest crop
                    grid[row][col] = EMPTY
                    coins += harvest_reward
                    # Uncomment when sound files are available:
                    # harvest_sound.play()

    # Update crop states based on timers
    current_time = time.time()
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            if grid[row][col] == PLANTED and current_time >= growth_timers[row][col]:
                grid[row][col] = GROWING
                growth_timers[row][col] = current_time + 5  # 5 more seconds to fully grow
                # Uncomment when sound files are available:
                # water_sound.play()
            elif grid[row][col] == GROWING and current_time >= growth_timers[row][col]:
                grid[row][col] = GROWN

    # Warning when coins are too low
    if coins < plant_cost:
        warning_text = font.render("Not enough coins to plant!", True, RED)
        screen.blit(warning_text, (WIDTH // 2 - 100, HEIGHT - 50))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
