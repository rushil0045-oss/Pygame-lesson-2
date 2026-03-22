import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((250, 250, 250))

PURPLE = (250, 0, 250)

pygame.draw.rect(window, PURPLE, (285, 200, 70, 80))

pygame.display.update()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()