import pygame

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()  # Controlling frame rate
# Font and Text
text_font = pygame.font.Font("UltimatePygameIntro copy/font/Pixeltype.ttf", 50)
text_Surface = text_font.render("My Runner Game!", False, "Black")
# Images needed

sky_Surface = pygame.image.load("UltimatePygameIntro copy/graphics/Sky.png").convert()
ground_Surface = pygame.image.load("UltimatePygameIntro copy/graphics/ground.png").convert()
snail_Surface = pygame.image.load("UltimatePygameIntro copy/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_Surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load("UltimatePygameIntro copy/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    # Quitting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print("collison")

    screen.blit(sky_Surface, (0, 0))
    screen.blit(ground_Surface, (0, 300))
    screen.blit(text_Surface, (500, 50))

    snail_rect.right -= 3
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(snail_Surface, snail_rect)
    screen.blit(player_surf, player_rect)
    """
    if player_rect.colliderect(snail_rect):
        print("Collison")

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)