import pygame
from random import choice
from player import Player
from enmey import Enmey
from bulet import BUllet
count2=1
count3=1
screen_height=700
screen_width=800
running=True
shoot=True
row=5
column=5
count=0
s_count=0
time=pygame.time.get_ticks()
class Game:

    global row ,column, screen,screen_width,screen_height
    def __init__(self):
        self.enmeys=pygame.sprite.Group()
        self.enmey_bulet=pygame.sprite.Group()
        self.player=pygame.sprite.Group()
        self.player_bulet=pygame.sprite.Group()
        self.right=True
        self.left= False
    def add(self):
        self.player.add(Player((screen_width/2)-25,screen_height-130,False,True))
        self.player.add(Player(0,screen_height-50,False,False))
        self.player.add(Player(60,screen_height-50,False,False))
        for y in range(1,row):
            for x in range(1,column):
                if y==1:self.enmeys.add(Enmey((x*60),(y*60),False,'green'))
                elif y==2:self.enmeys.add(Enmey((x*60),(y*60),False,'yellow'))
                elif y==3:self.enmeys.add(Enmey((x*60),(y*60),False,'red'))
                elif y==4:self.enmeys.add(Enmey((x*60),(y*60),False,'blue'))
    def enmey_move(self):
        enm = self.enmeys.sprites()
        self.enmeys.draw(screen)
        cont1=0
        for alien in enm:
            #print("movment")
            if self.right:
                    alien.rect.x += 1

            elif self.left:
                    alien.rect.x -= 1
            if alien.rect.right >= screen_width and cont1==3:
                 self.left=True
                 self.right=False
            elif alien.rect.left <= 0 and cont1==0:
                 self.left=False
                 self.right=True
            if (alien.hit):
                alien.kill()
            cont1+=1
    def player_move(self):
        global count2,count3,shoot
        keys=pygame.key.get_pressed()
        for play in self.player.sprites():
            if keys[pygame.K_a] and play.rect.x-1>=0 and play.active:
                play.rect.x-=1
            elif keys[pygame.K_d] and play.rect.x+51<=screen_width and play.active:
                play.rect.x+=1
            if play.hit:
                 play.destroy()
                 count2=2
                 count3=0
            if not(play.hit) and count2==2:
                 play.active=True
                 count2=1
            if play.active and count3==0:
                 shoot=False
                 if play.rect.x<((screen_width/2)-25):
                    play.rect.x+=1
                 elif play.rect.x>=((screen_width/2)-25):
                    if play.rect.y>((screen_height)-130):
                        play.rect.y-=1
                    elif play.rect.y<=((screen_height)-130):
                        shoot=True
                        count3=1
    def enmey_shoot(self):
        if self.enmeys.sprites():
               random_alien = choice(self.enmeys.sprites())
               bullet_sprite = BUllet(random_alien.rect.center)
               self.enmey_bulet.add(bullet_sprite)
    def player_shoot(self):
        if self.player.sprites():
            for play in self.player.sprites():
                if play.active:              
                    bullet_sprite = BUllet((play.rect.center))
                    self.player_bulet.add(bullet_sprite)
        
    def shoot(self):
        for bullet in self.enmey_bulet.sprites():
            bullet.rect.y+=5
        for bullet in self.player_bulet.sprites():
            bullet.rect.y-=5
    def contact(self):
        global shoot
        for bullet in self.enmey_bulet.sprites():
            for play in self.player.sprites():
                if not(shoot):
                    bullet.kill()
                if bullet.rect.y+15>=play.rect.y:
                    for a in range(int(bullet.rect.x),int(bullet.rect.x+4)):
                        for b in range(int(play.rect.x),int(play.rect.x+50)):
                            if a==b:
                                play.hit=True
                                play.active=False
                                bullet.kill()
                                b+=(play.rect.x+51)
                                a+=(bullet.rect.x+4)
                    if bullet.rect.y>=screen_height-68:
                        bullet.kill()
        for bullet in self.player_bulet.sprites():  
            for enmey in self.enmeys.sprites():
                if bullet.rect.y<=enmey.rect.y:
                    for c in range(int(bullet.rect.x),int(bullet.rect.x+4)):
                        for d in range(int(enmey.rect.x),int(enmey.rect.x+50)):
                            if c==d:
                                enmey.hit=True
                                bullet.kill()
                                d+=(enmey.rect.x+51)
                                c+=(bullet.rect.x+4)
                    if bullet.rect.y<=0:
                        bullet.kill()
    def draw(self):
        self.player.draw(screen)
        self.enmeys.draw(screen)
        pygame.draw.rect(screen,'Grey',(0,screen_height-68,screen_width,8))
        self.enmey_bulet.draw(screen)
        self.player_bulet.draw(screen)
game=Game()
        
#screen init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
ALIENLASER = pygame.USEREVENT + 1
pygame.time.set_timer(ALIENLASER,800)

#game loop
while running:
    keys=pygame.key.get_pressed()
    screen.fill((0,0,0))
    current_time=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running=False
        if event.type == ALIENLASER and shoot:
            game.enmey_shoot()
    if count==0:
        game.add()
        count+=1
    if keys[pygame.K_SPACE]:
        if (current_time-time)>=800:
            print("hi")
            game.player_shoot()
            time=pygame.time.get_ticks()
       
    game.contact()
    game.player_move()
    game.enmey_move()
    game.draw()
    game.shoot()
    pygame.display.flip()
    clock.tick(60)# fps
pygame.quit()