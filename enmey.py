import pygame
class Enmey(pygame.sprite.Sprite):
    def __init__(self,x,y,hit,color,column=5,screen_width=800):
        super().__init__()
        self.x=x
        self.y=y
        self.hit=hit
        self.column=column
        self.screen_width=screen_width
        self.left=True
        self.right=False
        file_path='images/'+color+'.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(50,40))
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
    def move(self,direction):
        print("movment1")
        self.rect.x += direction
    def destroy(self):
        self.kill()