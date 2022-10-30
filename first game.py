import pygame
x=pygame.init()
gamewindow=pygame.display.set_mode((800,500))
pygame.display.set_caption("snake eating")

game_over=False
exit_game=False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    print("you have pressed the right arrow key")
            if event.key==pygame.K_LEFT:
                print("you have pressed left arrow key")

pygame.quit()
quit()