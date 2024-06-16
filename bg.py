import pygame
class background(pygame.sprite.Sprite):
    def __init__(self,width,height,path='background'):
        super().__init__()
        file_path=f'images/{path}.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(width,height))
        self.rect=self.image.get_rect(topleft=(0,0))