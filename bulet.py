import pygame
class BUllet(pygame.sprite.Sprite):
    def __init__(self,file_path,pos=(0,0),pos_x=0,pos_y=0,wave_4=False,bullet_width=4,bullet_height=15):
        super().__init__()
        self.bullet_height=bullet_height
        self.bullet_width=bullet_width
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(bullet_width,bullet_height))
        if wave_4:
            self.rect = self.image.get_rect(topleft=(pos_x,pos_y))
        else:
            self.rect = self.image.get_rect(center = pos)
    def distroy(self):
        self.kill()