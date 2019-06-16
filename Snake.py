import pygame, random, os
from pygame import font

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,165,0)
DARK_CYAN = (0,204,204)
GREEN=(0,255,0)

def run():
    pygame.init()
    pygame.mixer.init()
    width = 600
    height = 600
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    cur_x = random.randint(30,width-30)
    cur_y = random.randint(30,height-30)
    food_x = 0
    food_y = 0

    while True:
        food_x = random.randint(30,width-30)
        food_y = random.randint(30,height-30)
        if food_x != cur_x and food_y != cur_y:
            break

    snake_width = 15
    velo_x = 0
    velo_y = 0
    fps = 30
    score = 0
    now = 1
    newscore_ishigh = False

    snake_len = 1
    snake=[]

    if (not os.path.exists("HighScore.txt")):
        with open("HighScore.txt","w") as f:
            f.write("0")

    highscore = gethighscore()
    exit = False
    over = False

    while not exit:
        if over:
            window.fill(BLACK)
            show_text(window,"Game Over!!!",ORANGE,245,100)
            if newscore_ishigh:
                show_text(window,"New High Score!!!",ORANGE,230,200)
                show_text(window,"Your score :: "+str(score),ORANGE,239,300)
            else:
                show_text(window,"Highscore :: "+str(highscore),ORANGE,241,200)
                show_text(window,"Your score :: "+str(score),ORANGE,239,300)
            show_text(window,"Press enter to play again",ORANGE,193,400)
            highscore = max(score,highscore)
            with open("HighScore.txt","w") as f:
                f.write(str(highscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        run()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    break
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

            if cur_x<0:
                cur_x = width
            if cur_x>width:
                cur_x=0
            if cur_y<0:
                cur_y = height
            if cur_y>height:
                cur_y=0

            if abs(cur_x+10-food_x)<10 and abs(cur_y+10-food_y)<10:
                score += 1
                now += 1
                snake_len += 3
                while True:
                    food_x = random.randint(30,width-30)
                    food_y = random.randint(30,height-30)
                    food=[]
                    food.append(food_x)
                    food.append(food_y)
                    if not food in snake:
                        break
                pygame.mixer.music.load('Eating.mp3')
                pygame.mixer.music.play()

            window.fill(BLACK)
            show_text(window,"Score :: "+str(score),DARK_CYAN,480,12)
            pygame.draw.circle(window,RED,(food_x, food_y), 10)

            head=[]
            head.append(cur_x)
            head.append(cur_y)
            snake.append(head)

            if len(snake)>snake_len:
                del(snake[0])

            if head in snake[:-1]:
                over = True
                pygame.mixer.music.load('Gameover.mp3')
                pygame.mixer.music.play()
                if(score>highscore):
                    newscore_ishigh = True
            draw_snake(window,WHITE ,snake, snake_width)
        now %= 11
        if not now:
            fps += 3
            now = 1
        pygame.display.update()
        clock.tick(fps)

def draw_snake(window,color, snake , size):
    for x,y in snake[:-1]:
        pygame.draw.rect(window,WHITE,[x, y, size, size])
    for x,y in reversed(snake):
        pygame.draw.rect(window,GREEN,[x, y, size, size])
        break

def gethighscore():
    with open("HighScore.txt","r") as f:
        p=int(f.read())
    return p

def show_text(window,text,color, x, y):
    myfont = pygame.font.Font('freesansbold.ttf',18)
    text = myfont.render(text,True,color)
    window.blit(text,(x,y))

run()
exit(0)
