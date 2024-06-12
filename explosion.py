import pygame
class Explosion(pygame.sprite.Sprite):
    def __init__(self,num,pos):
        super().__init__()
        self.num=num
        self.explosion_time=pygame.time.get_ticks()
        file_path=f'images/explosion{self.num}.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(50,50))
        self.rect = self.image.get_rect(center = pos)
    def called(self):
        self.explosion_time=pygame.time.get_ticks()