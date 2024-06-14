import pygame
class Bar(pygame.sprite.Sprite):
    def __init__(self,pos_x=750,pos_y=750,color=(255,0,0)):
        super().__init__()
        self.image = pygame.Surface((50,40))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(pos_x,pos_y))
    def distroy(self):
        self.kill()