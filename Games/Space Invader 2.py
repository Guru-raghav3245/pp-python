import pygame
import random

pygame.init()

# Set up the display
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))

# Load player and enemy images
player = pygame.image.load("space shooter.png")
enemy = pygame.image.load("space ufo.png")
bullet = pygame.image.load("bullet")

# Player coordinates and movement
playerX = 370
playerY = 450
playerX_change = 0
playerY_change = 0

# Enemy coordinates and movement
enemyX = random.randint(0, 800)
enemyY = 30
enemyX_change = 0.5
enemyY_change = 40

# Bullet coordinates and movement
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 1.5  # Adjust this value to control bullet speed
bullet_state = "ready"  # "ready" - ready to fire, "fire" - bullet is moving

# Functions to display player, enemy, and bullet
def player_fn(x, y):
    screen.blit(player, (x, y))

def enemy_fn(x, y):
    screen.blit(enemy, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))  # Adjust offsets for bullet position

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Update player position
    playerX += playerX_change

    # Ensure player stays within the screen boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Update enemy position
    enemyX += enemyX_change

    # Respawn enemy when it goes off-screen
    if enemyX >= 800:
        enemyX = random.randint(0, 736)
        enemyY += enemyY_change

    # Update bullet position
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Reset bullet position if it goes off-screen
    if bulletY <= 0:
        bulletY = 450
        bullet_state = "ready"

    # Display player, enemy, and bullet
    player_fn(playerX, playerY)
    enemy_fn(enemyX, enemyY)

    pygame.display.update()

