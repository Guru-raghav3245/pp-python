import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Ball properties
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = 5 * random.choice([-1, 1])

# Paddle properties
paddle_width = 15
paddle_height = 100
paddle_speed = 7

paddle1_x, paddle1_y = 0, height // 2 - paddle_height // 2
paddle2_x, paddle2_y = width - paddle_width, height // 2 - paddle_height // 2

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y *= -1

    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x *= -1

    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x *= -1

    if ball_x <= 0 or ball_x >= width:
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])

    win.fill(white)
    pygame.draw.rect(win, blue, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(win, blue, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(win, blue, (ball_x, ball_y), ball_radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
