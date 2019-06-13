import pygame, random
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

width = 600
height = 600
window = pygame.display.set_mode((width,height))

cur_x = random.randint(0,width)
cur_y = random.randint(0,height)

food_x = random.randint(50,width)
food_y = random.randint(50,height)

snake_width = 10
velo_x = 0
velo_y = 0
fps = 40
score = 0

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
                velo_x += 4
                velo_y = 0
            if event.key == pygame.K_LEFT:
                velo_x -= 4
                velo_y = 0
            if event.key == pygame.K_UP:
                velo_y -= 4
                velo_x = 0
            if event.key == pygame.K_DOWN:
                velo_y += 4
                velo_x = 0

    cur_x += velo_x
    cur_y += velo_y

    if abs(cur_x-food_x)<5 and abs(cur_y-food_y)<5:
        score += 1
        food_x = random.randint(50,width)
        food_y = random.randint(50,height)

    window.fill(BLACK)
    pygame.draw.rect(window,RED,[food_x, food_y, snake_width, snake_width])
    pygame.draw.rect(window,WHITE,[cur_x, cur_y, snake_width, snake_width])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

