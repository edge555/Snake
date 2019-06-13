import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

width = 600
height = 600
window = pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake")
pygame.display.update()
exit = False
over = False
while True:
    for event in pygame.event.get():
        print(event)
    window.fill(BLACK)
    pygame.display.update()

#pygame.quit()

