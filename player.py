import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,hit,active):
        super().__init__()
        self.x=x
        self.y=y
        self.hit=hit
        self.active=active
        file_path='sprites/player.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(50,40))
        self.rect=self.image.get_rect(topleft=(self.x,self.y))
    def destroy(self):
        self.kill()