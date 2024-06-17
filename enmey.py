import pygame
class Enmey(pygame.sprite.Sprite):
    def __init__(self,x,y,hit,type_,width=50,height=40):
        super().__init__()
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.hit=hit
        self.left=True
        self.right=False
        file_path='images/'+type_+'.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(width,height))
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
    def destroy(self):
        self.kill()