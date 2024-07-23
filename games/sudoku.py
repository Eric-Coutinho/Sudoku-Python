import pygame
import numpy as np

def generateGrid():
    row = 3
    col = 3
    grid = []

    for i in range(3):
        for j in range(3):
            cell = np.random.randint(1,9, size=(row, col))
            grid.append(cell)

generateGrid()

def playSudoku():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                pygame.key.get_pressed()[pygame.K_ESCAPE]):
                running = False

        screen.fill("#e3e3e3")

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
