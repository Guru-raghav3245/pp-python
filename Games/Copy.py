import pygame
import random

WIDTH = 500
HEIGHT = 500

def random_point():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    return (x, y)

def random_rects(n):
    rects = []
    for i in range(n):
        r = pygame.Rect(random_point(), (20, 20))
        rects.append(r)
    return rects

def no_rect(number):
    for i in range(number):
        pygame.draw.rect(random_rects(1))

# create routine for drawing the board

# create screen
pygame.init()


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('My Game Board in Python')

# color coding
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

fps = 60
noofrows = 2
noofcols = 2
size_of_box = 200
timer = pygame.time.Clock()
keys_map = {pygame.K_LEFT: (-10, 0), pygame.K_RIGHT: (10, 0), pygame.K_UP: (0, -10), pygame.K_DOWN: (0, 10)}

rect = pygame.Rect(100, 100, 200, 100)
rects = random_rects(100)

running = True
moving = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys_map:
                v = keys_map[event.key]
                rect.move_ip(v)


            elif event.key == pygame.K_r:
                rects_new = random_rects(20)
                for rec in rects_new:
                    pygame.draw.rect(screen, YELLOW, rec, 5)




        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False

        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    pygame.draw.rect(screen, RED, rect, 4)

    for r in rects:
        if rect.colliderect(r):
            # Inflate makes the rect bigger
            # pygame.draw.rect(screen, RED, r.inflate(10, 10), 5)
            # Clip cuts the rect to form 2
            # pygame.draw.rect(screen, GREEN, r.clip(rect), 0)
            pygame.draw.rect(screen, GREEN, r.union(rect), 0)

        else:
            pygame.draw.rect(screen, BLUE, r, 1)

    if moving:
        pygame.draw.rect(screen, RED, rect, 4)


    pygame.display.flip()
pygame.quit()