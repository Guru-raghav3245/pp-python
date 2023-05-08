import pygame

pygame.init()
import math
WIDTH = 500
HEIGHT = 500
blue = (0, 0, 225)
orange = (225, 100, 0)
white = (225, 225, 225)
green = (0, 200, 0)
# For the output screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('My Game Board in Python')

time = pygame.time.Clock()
run = True
while run:
    time.tick(60)
    pygame.display.flip()
    pygame.draw.rect(screen, orange, [0, 100, 500, 100])
    pygame.draw.rect(screen, white, [0, 200, 500, 100])
    pygame.draw.rect(screen,green , [0, 300, 500, 100])
    pygame.draw.circle(screen, blue, [250, 250], 50, 10)
    pygame.draw.circle(screen, blue, [250, 250], 1)

    for i in range(24):
        x = 250 + (50 * (math.cos(i)))
        y = 250 + (50 * (math.sin(i)))
        pygame.draw.line(screen, blue, [250, 250], [x, y])
        i += 15
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()