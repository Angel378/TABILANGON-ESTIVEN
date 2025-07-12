import pygame
import random

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball - TABILANGON E.")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont("Arial", 28, bold=True)

# Ball properties
ball_radius = 70  # Big ball
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_dx = 6
ball_dy = 5

# Ball color options
ball_colors = [
    (0, 0, 255),       # Blue
    (255, 0, 0),       # Red
    (0, 255, 0),       # Green
    (138, 43, 226),    # Violet
    (255, 255, 0)      # Yellow
]
ball_color = random.choice(ball_colors)

# Background color
bg_color = (0, 0, 0)  # Black

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    bounced = False

    # Bounce on screen edges
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx *= -1
        bounced = True
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1
        bounced = True

    # Change ball color on bounce
    if bounced:
        ball_color = random.choice(ball_colors)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Draw name "TABILANGON E." in the ball with white + black shadow
    text_shadow = font.render("TABILANGON E.", True, (0, 0, 0))        # Shadow (black)
    text_main = font.render("TABILANGON E.", True, (255, 255, 255))    # Main text (white)
    text_rect = text_main.get_rect(center=(ball_x, ball_y))
    screen.blit(text_shadow, (text_rect.x + 2, text_rect.y + 2))
    screen.blit(text_main, text_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
