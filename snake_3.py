import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)

# Clock and snake settings
clock = pygame.time.Clock()
block_size = 20
initial_speed = 5  # Start with a slower speed

# Font styles
font_style = pygame.font.Font(pygame.font.get_default_font(), 30)
score_font = pygame.font.Font(pygame.font.get_default_font(), 35)

# Display the score
def display_score(score):
    value = score_font.render(f"Score: {score}", True, white)
    screen.blit(value, [10, 10])


# Snake movement
def draw_snake(block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size], border_radius=5)


# Message on game over
def display_message(msg, color):
    message = font_style.render(msg, True, color)
    screen.blit(message, [width / 6, height / 3])


# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    snake_speed = initial_speed

    while not game_over:
        while game_close:
            screen.fill(black)
            display_message("Game Over! Press C to Restart or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = block_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)

        # Draw the food
        pygame.draw.ellipse(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1
            snake_speed += 0.2  # Increase speed gradually

        clock.tick(snake_speed)  # Adjust game speed dynamically

    pygame.quit()
    quit()


game_loop()

