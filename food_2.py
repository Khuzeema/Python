import pygame
import sys

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
BLUE = (0, 0, 255)        # Growing crop (watered)
YELLOW = (255, 255, 0)    # Fully grown crop
BLACK = (0, 0, 0)         # Grid lines

# Grid dimensions
GRID_ROWS, GRID_COLS = 5, 6
CELL_SIZE = 80
GRID_START_X, GRID_START_Y = 100, 100

# Crop states
EMPTY = 0
PLANTED = 1
GROWING = 2
GROWN = 3

# Initialize the farm grid (2D array)
grid = [[EMPTY for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
watered = [[False for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]  # Tracks watering status

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

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grid_pos = get_grid_position(pos[0], pos[1])
            if grid_pos:
                row, col = grid_pos
                if grid[row][col] == EMPTY:  # Plant crop
                    grid[row][col] = PLANTED
                elif grid[row][col] == PLANTED:  # Water crop
                    watered[row][col] = True
                    grid[row][col] = GROWING
                elif grid[row][col] == GROWING:  # Grow crop
                    if watered[row][col]:
                        grid[row][col] = GROWN
                        watered[row][col] = False
                elif grid[row][col] == GROWN:  # Harvest crop
                    grid[row][col] = EMPTY

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
