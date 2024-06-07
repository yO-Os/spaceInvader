import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,hit,active):
        super().__init__()
        self.x=x
        self.y=y
        self.hit=hit
        self.active=active
    def move(self,screen_width): 
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x-0.05>=0:
            self.x-=0.05
        elif keys[pygame.K_d] and self.x+50.05<=screen_width:
            self.x+=0.05