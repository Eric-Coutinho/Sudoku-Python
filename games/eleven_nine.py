# jogo_eleven_nine.py
import pygame

def playEleven_nine():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) 

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                pygame.key.get_pressed()[pygame.K_ESCAPE]):
                running = False

        screen.fill("purple")

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
