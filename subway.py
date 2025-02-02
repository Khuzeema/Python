import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_width, player_height = 50, 50
player_x = WIDTH // 4
player_y = HEIGHT - player_height - 10
player_speed = 8

# Obstacle properties
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 7
obstacle_list = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Add obstacles function
def add_obstacle():
    x_pos = random.randint(0, WIDTH - obstacle_width)
    obstacle_list.append([x_pos, -obstacle_height])

# Move obstacles function
def move_obstacles():
    global score
    for obstacle in obstacle_list[:]:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacle_list.remove(obstacle)
            score += 1

# Check collisions function
def check_collision(player_rect):
    for obstacle in obstacle_list:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if player_rect.colliderect(obstacle_rect):
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, GREEN, player_rect)

    # Obstacle logic
    if random.randint(1, 30) == 1:  # Add obstacles randomly
        add_obstacle()
    move_obstacles()

    # Draw obstacles
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Check for collisions
    if check_collision(player_rect):
        running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()
