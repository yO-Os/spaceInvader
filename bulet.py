import pygame
class BUllet(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((4,15))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = pos)
    def distroy(self):
        self.kill()