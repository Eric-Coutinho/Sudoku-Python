# jogo_eleven_nine.py
import pygame

def playSudoku():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                pygame.key.get_pressed()[pygame.K_ESCAPE]):
                running = False

        screen.fill("#e3e3e3")

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
