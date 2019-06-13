import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

width = 600
height = 600
window = pygame.display.set_mode((width,height))

cur_x = 50
cur_y = 20
snake_width = 10
velocity_x = 10
velocity_y = 10
fps = 40



pygame.display.set_caption("Snake")
pygame.display.update()
exit = False
over = False

clock = pygame.time.Clock()


while not exit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cur_x += 10
            if event.key == pygame.K_LEFT:
                cur_x -= 10
            if event.key == pygame.K_UP:
                cur_y -= 10
            if event.key == pygame.K_DOWN:
                cur_y += 10

    window.fill(BLACK)
    pygame.draw.rect(window,WHITE,[cur_x, cur_y, snake_width, snake_width])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

