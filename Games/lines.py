import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500
black = (0, 0, 0)
white = (225, 225, 225)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('My Game Board in Python')

time = pygame.time.Clock()

run = True
while run:
    time.tick(60)
    pygame.display.flip()
    pygame.draw.line(screen, white, [5, 10], [5, 50], 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()