import pygame
class Enmey(pygame.sprite.Sprite):
    def __init__(self,x,y,hit,color):
        super().__init__()
        self.x=x
        self.y=y
        self.hit=hit
        self.left=True
        self.right=False
        file_path='sprites/'+color+'.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(50,40))
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
    def move(self,colum,screen_width):
        if (self.x-0.05>0 and self.left):
            self.x-=0.05
        elif((self.x+60.05)*colum)<(screen_width) and self.right:
            self.x+=0.05
        if ((self.x+60.05)*colum)>screen_width:
            self.right=False
            self.left=True
        elif (self.x-0.5)<0:
            self.right=True
            self.left=False
