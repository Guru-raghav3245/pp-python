import pygame
import random

pygame.init()
# Title and caption
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# parameters order = height, width
screen = pygame.display.set_mode((800, 600))

# Player
player = pygame.image.load("space shooter.png")
# Coordinates
playerX = 370
playerY = 450
playerX_change = 0
playerY_change = 0

# Enemy
enemy = pygame.image.load("space ufo.png")

# Coordinates
enemyX = random.randint(0, 800)
enemyY = 30
enemyX_change = 0
enemyY_change = 0


# Player onto screen
def player_fn(x, y):
    screen.blit(player, (x, y))


# Enemy onto screen
def enemy_fn(x, y):
    screen.blit(enemy, (x, y))


# To make the screen stay and to close the screen
running = True
while running:
    # Changing the background
    # But keeping it black...
    screen.fill((0, 0, 0))
    # To make the screen stay and to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerY_change = 0
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerY_change = 0
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 700:
        playerX = 700
    if playerY <= 350:
        playerY = 350
    if playerY >= 600:
        playerY = 600

    player_fn(playerX, playerY)
    enemy_fn(enemyX, enemyY)
    pygame.display.update()
