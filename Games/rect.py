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
keys_map = {pygame.K_LEFT: (-5, 0), pygame.K_RIGHT: (5, 0), pygame.K_UP: (0, -5), pygame.K_DOWN: (0, 5)}

rect = pygame.Rect(100, 100, 200, 100)
rects = random_rects(50)

running = True
moving = False

while running:
    timer.tick(fps)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys_map:
                v = keys_map[event.key]
                rect.move_ip(v)
            elif event.key == pygame.K_r:
                new_rects = random_rects(20)
                for rec in new_rects:
                    pygame.draw.rect(screen, YELLOW, rec, 2)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False

        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)





    for r in rects:
        if rect.colliderect(r):
            #pygame.draw.rect(screen, RED, r, 2)
           # pygame.draw.rect(screen, RED, [-20, -20, -20, -20], 2)
            # pygame.draw.rect(screen, RED, r)
           common = r.clip(rect)
           pygame.draw.rect(screen, RED, common, 0)
       #     pygame.draw.rect(screen, RED, common, 0)
        else:
            pygame.draw.rect(screen, BLUE, r, 1)

    if moving:
        pygame.draw.rect(screen, RED, rect, 4)

    pygame.display.flip()

pygame.quit()
