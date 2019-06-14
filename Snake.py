import pygame, random
from pygame import font

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN=(0,255,0)

width = 600
height = 600
window = pygame.display.set_mode((width,height))

cur_x = random.randint(50,width-50)
cur_y = random.randint(50,height-50)

food_x = random.randint(50,width-50)
food_y = random.randint(50,height-50)

snake_width = 15
velo_x = 0
velo_y = 0
fps = 30
score = 0

pygame.display.set_caption("Snake")
pygame.display.update()
exit = False
over = False

snake=[]
snake_len = 1

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',18)

def show_score(text,color):
    text = font.render(text,True,color)
    window.blit(text,(480,25))

def draw_snake(window,color, snake , size):
    for x,y in snake:
        pygame.draw.rect(window,WHITE,[x, y, size, size])

while not exit:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velo_x += 5
                velo_y = 0
            if event.key == pygame.K_LEFT:
                velo_x -= 5
                velo_y = 0
            if event.key == pygame.K_UP:
                velo_y -= 5
                velo_x = 0
            if event.key == pygame.K_DOWN:
                velo_y += 5
                velo_x = 0

    cur_x += velo_x
    cur_y += velo_y

    if abs(cur_x-food_x)<10 and abs(cur_y-food_y)<10:
        score += 1
        snake_len += 3
        food_x = random.randint(50,width-50)
        food_y = random.randint(50,height-50)

    window.fill(BLACK)
    show_score("Score :: "+str(score),GREEN)

    head=[]
    head.append(cur_x)
    head.append(cur_y)
    snake.append(head)

    if len(snake)>snake_len:
        del(snake[0])

    pygame.draw.rect(window,RED,[food_x, food_y, snake_width, snake_width])
    draw_snake(window,WHITE ,snake, snake_width)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
