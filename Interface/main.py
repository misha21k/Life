import pygame

import Grid

SIZES = WIDTH, HEIGHT = (1200, 800)
FPS = 30

CELL = 100  # size of cell
X0, Y0 = 0, 0  # origin of coordinates

pygame.init()
screen = pygame.display.set_mode(SIZES, pygame.RESIZABLE)
pygame.display.set_caption("Life")
clock = pygame.time.Clock()

grid = Grid.Grid(x0=X0, y0=Y0, cell=CELL)

while True:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                grid.increase(*event.pos)
            elif event.button == 5:
                grid.decrease(*event.pos)

    # get width and height of window
    width, height = screen.get_size()

    # draw grid
    for x in range(grid.x1, width, grid.cell):
        pygame.draw.line(screen, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(grid.y1, height, grid.cell):
        pygame.draw.line(screen, pygame.Color('dimgray'), (0, y), (width, y))

    pygame.display.flip()
    clock.tick(FPS)
