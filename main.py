import pygame
from random import choice
from player import Player
from enmey import Enmey
from bulet import BUllet
first_ship,second_ship=False,False# first_ship:- the ship in the arena & second_ship:- the reserve lives
screen_height=700
screen_width=800
running=True# Whether the program is running or not
shoot=True# If it is able to shoot or not(space ship)
row=5# Aliens
column=5# Aliens
count=0# helps start the game
time=pygame.time.get_ticks()#  time when the game starts
#  used to add game components and function to the game
class Game:

    global row ,column, screen,screen_width,screen_height
    def __init__(self):
        self.enmeys=pygame.sprite.Group()#  creates a group to add the enmey ship
        self.enmey_bulet=pygame.sprite.Group()#  creates a group to add the enmey bullet
        self.player=pygame.sprite.Group()#  creates a group to add the player ship
        self.player_bulet=pygame.sprite.Group()#  creates a group to add the player bullet
        #  bools that indicates the direction of the enmey
        self.right=True
        self.left= False

#  creates and adds the objects to their respective groups
    def add(self):
        self.player.add(Player((screen_width/2)-25,screen_height-130,False,True))#  The true value signifies the ship is in the arena
        self.player.add(Player(0,screen_height-50,False,False))
        self.player.add(Player(60,screen_height-50,False,False))
        for y in range(1,row):
            for x in range(1,column):
                if y==1:self.enmeys.add(Enmey((x*60),(y*60),False,'green'))
                elif y==2:self.enmeys.add(Enmey((x*60),(y*60),False,'yellow'))
                elif y==3:self.enmeys.add(Enmey((x*60),(y*60),False,'red'))
                elif y==4:self.enmeys.add(Enmey((x*60),(y*60),False,'blue'))
#  moves the enmey ships
    def enmey_move(self):
        self.enmeys.draw(screen)
        for alien in self.enmeys.sprites():
            if self.right:
                    alien.rect.x += 1
            elif self.left:
                    alien.rect.x -= 1
            if alien.rect.right >= screen_width:
                 self.left=True
                 self.right=False
            elif alien.rect.left <= 0:
                 self.left=False
                 self.right=True
            if (alien.hit):
                alien.kill()
    def player_move(self):
        global first_ship,second_ship,shoot
        keys=pygame.key.get_pressed()
        for play in self.player.sprites():
            if keys[pygame.K_a] and play.rect.x-1>=0 and play.active and shoot:
                play.rect.x-=1
            elif keys[pygame.K_d] and play.rect.x+51<=screen_width and play.active and shoot:
                play.rect.x+=1
            if play.hit:
                 play.destroy()
                 first_ship=True
                 second_ship=True
            if not(play.hit) and first_ship:
                 play.active=True
                 first_ship=False
            if play.active and second_ship:
                 shoot=False
                 if play.rect.x<((screen_width/2)-25):
                    play.rect.x+=3
                 elif play.rect.x>=((screen_width/2)-25):
                    if play.rect.y>((screen_height)-130):
                        play.rect.y-=1
                    elif play.rect.y<=((screen_height)-130):
                        shoot=True
                        second_ship=False
    def enmey_shoot(self):
        if self.enmeys.sprites():
               random_alien = choice(self.enmeys.sprites())
               self.enmey_bulet.add(BUllet(random_alien.rect.center))
    def player_shoot(self):
        if self.player.sprites():
            for play in self.player.sprites():
                if play.active:              
                    self.player_bulet.add(BUllet((play.rect.center)))
        
    def shoot(self):
        for bullet in self.enmey_bulet.sprites():
            bullet.rect.y+=9
        for bullet in self.player_bulet.sprites():
            bullet.rect.y-=9
    def contact(self):
        global shoot
        for bullet in self.enmey_bulet.sprites():
            for play in self.player.sprites():
                if not(shoot):
                    bullet.kill()
                if bullet.rect.y+15>=play.rect.y:
                    for a in range(int(bullet.rect.x),int(bullet.rect.x+4)):
                        for b in range(int(play.rect.x),int(play.rect.x+50)):
                            if a==b and play.active:
                                play.hit=True
                                play.active=False
                                b+=(play.rect.x+51)
                                a+=(bullet.rect.x+4)
                                bullet.kill()
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
        if (current_time-time)>=800 and shoot:
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