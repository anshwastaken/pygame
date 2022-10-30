
import pygame
import random
from pygame import mixer

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
orange=(255,165,0)
purple = (128,0,128)

# Creating window
screen_width = 750
screen_height = 750
gameWindow = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('Untitled design (5).png')
aftergame = pygame.image.load('good game broooo.png')
beforegame = pygame.image.load('press space bar to.png')


# Game Title
pygame.display.set_caption("UNFAIR SNAKE")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x=0
velocity_y=0
food_x = random.randint(0,screen_width-20)
food_y = random.randint(0,screen_height-20)
obstacle_x = random.randint(0,screen_width-20)
obstacle_y = random.randint(0,screen_height-20)
score=0
snake_size = 10
fps = 40
mixer.music.load('drive_forever.mp3')
mixer.music.play(-1)

clock = pygame.time.Clock()
font=pygame.font.SysFont(None,40)
def text_screen(text, color , x , y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_lst,snake_size):
    for x,y in snk_lst:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_lst=[]
snk_length=1

def welcome():
    exit_game = False
    while not exit_game:


        for event in pygame.event.get():
            gameWindow.fill((0, 0, 0))
            gameWindow.blit(beforegame, (0, 0))
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_lst = []
    snk_length = 1
    with open("high score.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(4, screen_width-20)
    food_y = random.randint(2, screen_height-20)
    obstacle_x = random.randint(2,screen_width-20)
    obstacle_y = random.randint(2,screen_height-20)
    score = 0
    snake_size = 10
    fps = 30
    while not exit_game:
        if game_over:
            with open("high score.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.blit(aftergame,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        game_over = True



            snake_x= snake_x + velocity_x
            snake_y= snake_y + velocity_y

            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score += 5
                sound = mixer.Sound('voice.mp3')
                sound.play()
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                obstacle_x = random.randint(20, screen_width / 2)
                obstacle_y = random.randint(20, screen_height / 2)


                snk_length+=3
                if score > int(hiscore):
                    hiscore = score

            if abs(snake_x-obstacle_x)<6 and abs(snake_y-obstacle_y)<6:
                soundd = mixer.Sound('GOOGLE_SNAKE_DEATH_EARRAPE_(getmp3.pro).mp3')
                soundd.play()
                game_over = True

            if snake_x == 50 and snake_y == 55:
                pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])


            gameWindow.fill(black)
            gameWindow.blit(background,(0,0))
            text_screen("score:" +str(score) + "  High score: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [obstacle_x, obstacle_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if score==50:
                fps = 50

            if len(snk_lst)>snk_length:
                del snk_lst[0]

            if head in snk_lst[:-1]:
                soundd = mixer.Sound('GOOGLE_SNAKE_DEATH_EARRAPE_(getmp3.pro).mp3')
                soundd.play()
                game_over= True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                soundd = mixer.Sound('GOOGLE_SNAKE_DEATH_EARRAPE_(getmp3.pro).mp3')
                soundd.play()
                game_over=True
                print("game over")


            plot_snake(gameWindow, blue, snk_lst, snake_size)
            if score >= 100:
                plot_snake(gameWindow, purple, snk_lst, snake_size)
                fps = 60;
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
gameloop()
