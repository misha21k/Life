import pygame

import Grid
from Settlement import Settlement

SIZES = WIDTH, HEIGHT = (1200, 800)
FPS = 30

CELL = 100  # size of cell
X0, Y0 = 0, 0  # origin of coordinates

pygame.init()
screen = pygame.display.set_mode(SIZES, pygame.RESIZABLE)
pygame.display.set_caption("Life")
clock = pygame.time.Clock()

grid = Grid.Grid(x0=X0, y0=Y0, cell=CELL)

settlement = Settlement.Settlement()
being = Settlement.Being(1, 2)
settlement.add_being(being)


while True:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                grid.increase(*event.pos)  # increase of grid's size
            elif event.button == 5:
                grid.decrease(*event.pos)  # decrease of grid's size
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            grid.move(*event.rel)  # move grid by mouse

    # get width and height of window
    width, height = screen.get_size()

    # draw grid
    for x in range(grid.x1, width, grid.cell):
        pygame.draw.line(screen, pygame.Color('dimgray'), (x, 0), (x, height))
    for y in range(grid.y1, height, grid.cell):
        pygame.draw.line(screen, pygame.Color('dimgray'), (0, y), (width, y))

    # draw settlement
    for being in settlement:
        being = Grid.Coordinates(being.x, being.y)
        being = grid.origin + being * grid.cell + Grid.Coordinates(1, 1)
        pygame.draw.rect(screen, pygame.Color('green'), (being.x, being.y, grid.cell-1, grid.cell-1))

    pygame.display.flip()
    clock.tick(FPS)
