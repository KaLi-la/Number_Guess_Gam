import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game variables
ball_x = random.randint(50, WIDTH - 50)
ball_y = 50
ball_radius = 20
ball_speed = 5

player_x = WIDTH // 2
player_y = HEIGHT - 50
player_width = 100
player_height = 20
player_speed = 10

score = 0
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move ball
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_x = random.randint(50, WIDTH - 50)
        ball_y = 50
        score -= 1  # Penalty for missing the ball

    # Check collision
    if (player_x < ball_x < player_x + player_width and
            player_y < ball_y < player_y + player_height):
        ball_x = random.randint(50, WIDTH - 50)
        ball_y = 50
        score += 1  # Reward for catching the ball

    # Draw objects
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
