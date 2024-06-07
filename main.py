import pygame
from random import choice
from player import Player
from enmey import Enmey
screen_height=700
screen_width=800
running=True
row=4
column=4
def game():
    global row ,column, screen
    enmey=pygame.sprite.Group()
    enmey_bulet=pygame.sprite.Group()
    for x in range(1,row):
        for y in range(1,column):
            if x==1:enmey.add(Enmey((x*60),(y*50)),False,'green')
            elif x==2:enmey.add(Enmey((x*60),(y*50)),False,'yellow')
            elif x==3:enmey.add(Enmey((x*60),(y*50)),False,'red')
            elif x==2:enmey.add(Enmey((x*60),(y*50)),False,'blue')
    enmey.draw(screen)
#screen init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


#game loop
while running:
    screen.fill((0,0,0))
    game()
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running=False
    pygame.display.flip()
    clock.tick(60)# fps
pygame.quit()