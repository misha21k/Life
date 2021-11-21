import pygame

SIZES = WIDTH, HEIGHT = (1200, 800)
tile = 10
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SIZES, pygame.RESIZABLE)
pygame.display.set_caption("Life")
clock = pygame.time.Clock()

while True:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                tile *= 1.1
            if event.button == 5:
                tile /= 1.1

    # get width and height of window
    width, height = screen.get_size()

    # draw grid
    for x in range(0, width, int(tile)):
        pygame.draw.line(screen, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(0, height, int(tile)):
        pygame.draw.line(screen, pygame.Color('dimgray'), (0, y), (width, y))

    # change size of window

    # change scale of grid

    pygame.display.flip()
    clock.tick(FPS)
