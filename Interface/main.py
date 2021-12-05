import pygame

import Grid
from Settlement import Settlement

SIZES = WIDTH, HEIGHT = (1200, 800)  # sizes of window
FPS = 30
UPDATE = 5  # frequency of settlement's update

CELL = 40  # size of cell
X0, Y0 = 0, 0  # origin of coordinates

BLACK = pygame.Color('black')
DIMGRAY = pygame.Color('dimgray')
GREEN = pygame.Color('green')

pygame.init()
screen = pygame.display.set_mode(SIZES, pygame.RESIZABLE)
pygame.display.set_caption("Game Life")
clock = pygame.time.Clock()

grid = Grid.Grid(x0=X0, y0=Y0, cell=CELL)
pause = True  # to set play on pause
settlement = Settlement.Settlement()  # empty settlement
count = 0

while True:
    screen.fill(BLACK)
    count = 0 if count == UPDATE else count + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                grid.increase(*event.pos)  # increase of grid's size
            elif event.button == 5:
                grid.decrease(*event.pos)  # decrease of grid's size
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and pause:
                # add or delete cell (being) on grid by mouse
                being = (Grid.Coordinates(*event.pos) - grid.origin) // grid.cell
                being = Settlement.Being(being.x, being.y)
                if being in settlement:
                    settlement.remove_being(being)
                else:
                    settlement.add_being(being)
        elif event.type == pygame.MOUSEMOTION and event.buttons[2]:
            grid.move(*event.rel)  # move grid by mouse
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pause = not pause  # set game in pause
            elif event.key == pygame.K_BACKSPACE and pause:
                settlement.clear()  # clear grid

    # next generation for settlement
    if not pause and count == UPDATE:
        settlement.calculate_next_generation()

    # get width and height of window
    width, height = screen.get_size()

    # draw grid
    for x in range(grid.x1, width, grid.cell):
        pygame.draw.line(screen, DIMGRAY, (x, 0), (x, height))
    for y in range(grid.y1, height, grid.cell):
        pygame.draw.line(screen, DIMGRAY, (0, y), (width, y))

    # draw settlement
    for being in settlement:
        being = Grid.Coordinates(being.x, being.y)
        being = grid.origin + being * grid.cell + Grid.Coordinates(1, 1)
        pygame.draw.rect(screen, GREEN, (being.x, being.y, grid.cell-1, grid.cell-1))

    pygame.display.flip()
    clock.tick(FPS)
