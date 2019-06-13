import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

width = 600
height = 600
window = pygame.display.set_mode((width,height))

start_x = 50
start_y = 20
snake_width = 10

pygame.display.set_caption("Snake")
pygame.display.update()
exit = False
over = False
while not exit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit = True

    window.fill(BLACK)
    pygame.draw.rect(window,WHITE,[start_x, start_y, snake_width, snake_width])
    pygame.display.update()

pygame.quit()

