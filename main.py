import pygame
from random import choice
from player import Player
from enmey import Enmey
from bulet import BUllet
from bg import background
from explosion import Explosion
from bar import Bar
import pygame.mixer as mixer
mixer.init()
pygame.font.init()
first_ship,second_ship=False,False
screen_height=800
screen_width=1000
wave_1=True
wave_2=False
wave_3=False
wave_4=False
running=True
shoot=True
count=0
setting_count=0
border1=0
border2=screen_width/2
life=3
bullet_speed=7
num_enmeys=9
ship_speed=1
ship_width=50
ship_height=40
time=pygame.time.get_ticks()
recharge_time=pygame.time.get_ticks()
laser_sound = mixer.Sound("images/laser-gun.mp3")
explosion_sound=mixer.Sound("images/explosion.mp3")
background_sound=mixer.Sound("images/background-music.mp3")
choose_ship=False
ship_option='player'
arrow='setting'
unmute=True
mute=False
help=False
in_game=False
select=mixer.Sound("images/select.mp3")
navigate=mixer.Sound("images/navigate.mp3")
font=pygame.font.SysFont('Arial',32)
play_color=(255,0,0)
help_color=(0,255,0)
ship_color=(0,255,0)
exit_color=(0,255,0)
retry_color=(0,255,0)
play_pos=screen_width/2
help_pos=screen_width/2
ship_pos=screen_width/2
exit_pos=screen_width/2
retry_pos=screen_width/2
diamond=['  x',
         ' x x',
         'x x x',
         ' x x',
         '  x']
rectangle=[ 'x x x x',
            'x x x x',
            'x x x x',
            'x x x x',
            'x x x x']
crown=[ 'x  x  x',
        'xxx xxx',
        'xxxxxxx',
        'xxxxxxx']
#  used to add game components and function to the game
background_sound.play()
class Game:

    global row ,column, screen,screen_width,screen_height,border2,border1,life,diamond,rectangle,num_enmeys,bullet_speed,ship_speed
    def __init__(self):
        self.enmeys=pygame.sprite.Group()#  creates a group to add the enmey ship
        self.enmey_bulet=pygame.sprite.Group()#  creates a group to add the enmey bullet
        self.player=pygame.sprite.Group()#  creates a group to add the player ship
        self.player_bulet=pygame.sprite.Group()#  creates a group to add the player bullet
        self.background=pygame.sprite.Group()
        self.explosion=pygame.sprite.Group()
        self.shield=pygame.sprite.Group()
        self.process_bar=pygame.sprite.Group()
        self.shape = diamond
        #  bools that indicates the direction of the enmeys ship
        self.right=True
        self.left= False

#  creates and adds the objects to their respective groups
    def add(self,x_start=100,y_start=10):
        global bullet_speed,ship_speed,ship_height,ship_width
        if wave_1:
            self.shape = diamond
            self.background.add(background(screen_width,screen_height))
            self.player.add(Player((screen_width/2)-25,screen_height-130,False,True,ship_option))#  The true value signifies the ship is in the arena
            self.player.add(Player(0,screen_height-50,False,False,ship_option))
            self.player.add(Player(60,screen_height-50,False,False,ship_option))
            self.shield.add(Enmey(screen_width-300,screen_height-50,False,'disabled-shield'))
            self.process_bar.add(Bar())
        elif wave_2:
            self.shape=rectangle
            ship_speed+=1
            bullet_speed+=1
        elif wave_3:
            self.shape=crown
            ship_speed+=1
            bullet_speed+=1
        if wave_4:
            self.enmeys.add(Enmey(120,60,False,'extra',150,100))
            ship_width=150
            ship_height=100
        else:
            for row_index, row in enumerate(self.shape):
                    for col_index , col in enumerate(row):
                         if col == 'x':
                              x = x_start +(col_index * 60)
                              y = y_start + (row_index * 60)
                              self.enmeys.add(Enmey(x,y,False,'green'))
#  moves the enmey ships
    def enmey_move(self):
        global num_enmeys,row
        #the loop is used to access each object in the enmey group
        for alien in self.enmeys.sprites():
             #makes the enmey ship move to the right
            if self.right :
                 alien.rect.x += ship_speed
             #makes the enmey ship move to the left
            elif self.left:
                 alien.rect.x -= ship_speed
             #checkes if the ship in the most right ship reached the right of frame
            if alien.rect.right >= screen_width:
                 self.left=True
                 self.right=False
                 for alien in self.enmeys.sprites():
                    alien.rect.y += 20
            #checkes if the ship in the most left ship reached the left of frame
            elif alien.rect.left <= 0:
                 self.left=False
                 self.right=True
                 for alien in self.enmeys.sprites():
                    alien.rect.y += 20
            #kills the enmey ship that have been hit
            if (alien.hit):
                num_enmeys-=1
                if not(wave_4):
                    alien.kill()
                if wave_4:
                    alien.hit=False 
                    if num_enmeys==0:
                        alien.kill()
#  moves the player ships
    def player_move(self):
        global first_ship,second_ship,shoot,border2,border1,ship_speed,recharge_time,current_time#imports global variable for use
        keys=pygame.key.get_pressed()#gets the key pressed from the keyboard
        #the loop is used to access each object in the player group
        if current_time-recharge_time<=2000:
            print(current_time-recharge_time)
            if current_time-recharge_time<=500:
               for bar in self.process_bar.sprites():
                   bar.kill()
               self.process_bar.add(Bar()) 
            elif current_time-recharge_time>500 and current_time-recharge_time<=1000:
               for bar in self.process_bar.sprites():
                   bar.kill()
               for x in range(1,3):
                   self.process_bar.add(Bar((50*x)+(screen_width-300)))
            elif current_time-recharge_time>1000 and current_time-recharge_time<=1500:
               for bar in self.process_bar.sprites():
                   bar.kill()
               for x in range(1,4):
                   self.process_bar.add(Bar((50*x)+(screen_width-300)))
            elif current_time-recharge_time>1500 and current_time-recharge_time<=2000:
               for bar in self.process_bar.sprites():
                   bar.kill()
               for x in range(1,5):
                   self.process_bar.add(Bar((50*x)+(screen_width-300),750,(0,255,0)))
        for play in self.player.sprites():

            #checks if the player reached the left frame if it did't enables the ship to move to the left
            if keys[pygame.K_a] and play.rect.x-1>=0 and play.active and shoot:
                play.rect.x-=ship_speed

            #checks if the player reached the right frame if it did't enables the ship to move to the right
            elif keys[pygame.K_d] and play.rect.x+51<=screen_width and play.active and shoot:
                play.rect.x+=ship_speed

            #kills the player when hit
            if play.hit:
                 play.destroy()
                 first_ship=True
                 second_ship=True

            #checks if the active ship is distroyed and makes the next ship active
            if not(play.hit) and first_ship:
                 play.active=True
                 first_ship=False

            #checks if the active ship is under the wall
            if play.active and second_ship:
                 shoot=False

                 #moves the ship to the center of the wall to the left
                 if play.rect.x<((screen_width/2)-25):
                    play.rect.x+=3

                #checks if the ship is in front of the door
                 elif play.rect.x>=((screen_width/2)-25):

                    #opens the door
                    if border1>-25 and border2<((screen_width/2)+25) and play.rect.y>((screen_height)-130):
                        border1-=2
                        border2+=2

                    #moves the ship through the door
                    elif play.rect.y>((screen_height)-130):
                        play.rect.y-=1
                    
                    #checks if the ship passed through the door
                    elif play.rect.y<=((screen_height)-130):

                        #closes the door
                        if border1<0 and border2>((screen_width/2)):
                            border1+=2
                            border2-=2
                        
                        #enables shooting
                        else:
                            shoot=True
                            second_ship=False
#  no comment
    def enmey_shoot(self):
        global charged,ship_height,ship_speed,ship_width,huge_laser,charge_sound
        if self.enmeys.sprites():
               if not(wave_4):
                    random_alien = choice(self.enmeys.sprites())#chooses random enmey to shoot the bullets
                    self.enmey_bulet.add(BUllet('images/enemy-laser.png',random_alien.rect.center))#creates the bullet
                    laser_sound.play()
               else:
                    for alien in self.enmeys.sprites():
                        self.enmey_bulet.add(BUllet('images/enemy-laser.png',(0,0),alien.rect.x+(ship_width/3)-10,alien.rect.y+ship_height,True))
                        laser_sound.play()
                        self.enmey_bulet.add(BUllet('images/enemy-laser.png',(0,0),alien.rect.x+(ship_width/2)+5,alien.rect.y+ship_height-30,True))
                        laser_sound.play()
                        self.enmey_bulet.add(BUllet('images/enemy-laser.png',(0,0),alien.rect.x+(ship_width)-30,alien.rect.y+ship_height,True))
                        laser_sound.play()                                                                                  
#      
    def player_shoot(self):
        if self.player.sprites():
            #the loop is used to access each object in the player group
            for play in self.player.sprites():

                #checks if the player is on the field
                if play.active:              
                    self.player_bulet.add(BUllet('images/player-laser.png',play.rect.center))#creates the bullet
#  moves the bullets
    def shoot(self):
        global life,laser_sound,bullet_speed

        #iterates through each enmey bullet
        for bullet in self.enmey_bulet.sprites():           
            bullet.rect.y+=bullet_speed#  moves the bullets of the enmey

        #checks if the player have used all its life
            if life==0:
                bullet.kill()#distroies the enmeys bullet
        #iterates through each enmey bullet
        for bullet in self.player_bulet.sprites():
        #checks if the player have used all its life
            if life==0:
                bullet.kill()#distroies the players bullet
            bullet.rect.y-=bullet_speed#  moves the bullets of the player
#   checks bullet contact  
    def contact(self):
        global shoot,life,explosion_sound,current_time,num_enmeys,ship_width,ship_height #imports global variable for use
        for exploded in self.explosion.sprites():
            
            if (exploded.num+2<4 and current_time-exploded.explosion_time>=500):
                self.explosion.add(Explosion(exploded.num+2,exploded.rect.center))
                exploded.kill()
            elif exploded.num+2>4 and (current_time-exploded.explosion_time>500):
                exploded.kill()
        #iterates through the enmeys bullet
        for bullet in self.enmey_bulet.sprites():
            #iterates through the player group
            for play in self.player.sprites():
                if not(shoot):
                    bullet.kill()
                #iterates through each point of the enmey bullets height
                for height_bullet in range(bullet.rect.y,bullet.rect.y+bullet.bullet_height):
                    #iterates through each point of the player ships height
                    for height_player in range(play.rect.y,play.rect.y+50):
                        #checks if the bullet and the ship are on the same position vertically(y-axsis)
                        if height_bullet==height_player:
                            #iterates through each point of the enmey bullets width
                            for a in range(int(bullet.rect.x),int(bullet.rect.x+bullet.bullet_width)):
                                #iterates through each point of the player ships width
                                for b in range(int(play.rect.x),int(play.rect.x+50)):
                                    #checks if the bullet and the ship are on the same position horizontally(x-axsis)
                                    if a==b and play.active:
                                        life-=1
                                        play.hit=True
                                        play.active=False
                                        self.explosion.add(Explosion(1,play.rect.center))
                                        for explod in self.explosion.sprites():
                                            explod.called()
                                        b+=(play.rect.x+51)
                                        a+=(bullet.rect.x+4)
                                        explosion_sound.play()
                                        bullet.kill()
            #prevents the bullet from passing the wall
            if bullet.rect.y>=screen_height-68:
                bullet.kill()
        #does the same thing as the above loop but it checks if the enmey ship is hit
        for bullet in self.player_bulet.sprites():  
            for enmey in self.enmeys.sprites():
                for height_p_bullet in range(bullet.rect.y,bullet.rect.y+16):
                    for height_ship in range(enmey.rect.y,enmey.rect.y+ship_height):
                        if height_p_bullet==height_ship:
                            for c in range(int(bullet.rect.x),int(bullet.rect.x+4)):
                                for d in range(int(enmey.rect.x),int(enmey.rect.x+ship_width)):
                                    if c==d:
                                        
                                        enmey.hit=True
                                        self.explosion.add(Explosion(1,enmey.rect.center))
                                        for explod1 in self.explosion.sprites():
                                            explod1.called()
                                        explosion_sound.play()
                                        bullet.kill()
                                        d+=(enmey.rect.x+51)
                                        c+=(bullet.rect.x+4)
                            if bullet.rect.y<=0:
                                bullet.kill()
    def draw(self):
        self.background.draw(screen)
        self.explosion.draw(screen)
        self.player.draw(screen)#displays the player ship
        self.enmeys.draw(screen)#displays the enmeys ship
        #displays the wall
        pygame.draw.rect(screen,'Grey',(border1,screen_height-68,screen_width/2,8))
        pygame.draw.rect(screen,'Grey',(border2,screen_height-68,screen_width/2,8))

        self.enmey_bulet.draw(screen)#displays the enmeys bullet
        self.player_bulet.draw(screen)#displays the players bullet
        self.shield.draw(screen)
        self.process_bar.draw(screen)

game=Game()
class Setting:
    global choose_ship
    def __init__(self):
        self.setting=pygame.sprite.Group()#  creates a group to add the enmey ship
        self.ship=pygame.sprite.Group()
        self.bullet=pygame.sprite.Group()
        self.music=pygame.sprite.Group()
    def add(self):
        self.setting.add(Enmey((screen_width/2)-50,300,False,arrow,30,30))
        self.music.add(Enmey(screen_width-120,screen_height-120,False,'unmute',100,100))
    def move(self):
        keyy=pygame.key.get_just_released()
        kyy=pygame.key.get_pressed()
        for bullet in self.bullet:
            bullet.rect.y-=6
        for setting in self.setting.sprites():
            if keyy[pygame.K_w]  and (setting.rect.y>300 or count!=0) and setting.rect.y>250 and setting.rect.y!=screen_height-75:
                navigate.play()
                setting.rect.y-=50
            if keyy[pygame.K_s] and setting.rect.y<450:
                navigate.play()
                setting.rect.y+=50
            elif keyy[pygame.K_s] and setting.rect.y==450:
                navigate.play()
                setting.rect.x=screen_width-160
                setting.rect.y=screen_height-75
            if keyy[pygame.K_w] and setting.rect.y==screen_height-75:
                navigate.play()
                setting.rect.x=(screen_width/2)-50
                setting.rect.y=450
            if keyy[pygame.K_a] and setting.rect.x>275 and choose_ship:
                navigate.play()
                setting.rect.x-=200
            if keyy[pygame.K_d] and setting.rect.x<675 and choose_ship:
                navigate.play()
                setting.rect.x+=200
            if kyy[pygame.K_a] and setting.rect.x-2>0 and help:
                setting.rect.x-=2
            if kyy[pygame.K_d] and setting.rect.x+2<screen_width and help:
                setting.rect.x+=2
            if keyy[pygame.K_SPACE] and setting.rect.x+2<screen_width and help:
                self.bullet.add(BUllet('images/player-laser.png',setting.rect.center))              
    def fun(self):
        global in_game,help,choose_ship,ship_option,arrow,running,count,num_enmeys,wave_1,wave_2,wave_3,wave_4,life,border1,border2,mute,unmute
        keyy=pygame.key.get_just_released()
        if keyy[pygame.K_f]:
            if choose_ship:
                choose_ship=False
                
                for setting in self.setting.sprites():
                    if setting.rect.x==475:
                        select.play()
                        ship_option='player2'
                        arrow='setting2'
                    elif setting.rect.x==675:
                        select.play()
                        ship_option='player3'
                        arrow='setting3'
                    elif setting.rect.x==275:
                        select.play()
                        ship_option='player'
                        arrow='setting'
                    for new in game.enmeys.sprites():
                        new.kill()
                    for new in game.player.sprites():
                        new.kill()
                    for new in game.enmey_bulet.sprites():
                        new.kill()
                    for new in game.player_bulet.sprites():
                        new.kill()
                    for new in game.explosion.sprites():
                        new.kill()
                    count=0
                    num_enmeys=9
                    wave_1=True
                    wave_2=False
                    wave_3=False
                    wave_4=False
                    life=3
                    border1=0
                    border2=screen_width/2
                    setting.kill()
                for ship in self.ship.sprites():
                    ship.kill()
                self.setting.add(Enmey((screen_width/2)-50,400,False,arrow,30,30))
            else:
                for setting in self.setting.sprites():
                    print("enter")
                    if setting.rect.y==250:
                        select.play()
                        for new in game.enmeys.sprites():
                            new.kill()
                        for new in game.player.sprites():
                            new.kill()
                        for new in game.enmey_bulet.sprites():
                            new.kill()
                        for new in game.player_bulet.sprites():
                            new.kill()
                        for new in game.explosion.sprites():
                            new.kill()
                        count=0
                        in_game=True
                        num_enmeys=9
                        wave_1=True
                        wave_2=False
                        wave_3=False
                        wave_4=False
                        life=3
                        border1=0
                        border2=screen_width/2
                    elif setting.rect.y==300:
                        select.play()
                        in_game=True
                    elif setting.rect.y==350:
                        select.play()
                        for settng in self.setting.sprites():
                            settng.kill()
                        self.setting.add(Enmey(screen_width/2,(screen_height-130),False,ship_option,50,50))
                        help=True
                    elif setting.rect.y==400:
                        select.play()
                        choose_ship=True
                        setting.kill()
                        self.ship.add(Enmey(200,300,False,'player',200,200))
                        self.ship.add(Enmey(400,300,False,'player2',200,200))
                        self.ship.add(Enmey(600,300,False,'player3',200,200))
                        self.setting.add(Enmey(475,510,False,ship_option,50,50))
                    elif setting.rect.y==450:
                        select.play()
                        running=False
                    elif setting.rect.y==screen_height-75 and unmute:
                        select.play()
                        for music in self.music.sprites():
                            music.kill()
                        self.music.add(Enmey(screen_width-120,screen_height-120,False,'mute',100,100))
                        background_sound.stop()
                        unmute=False
                        mute=True
                    elif setting.rect.y==screen_height-75 and mute:
                        select.play()
                        for music in self.music.sprites():
                            music.kill()
                        self.music.add(Enmey(screen_width-120,screen_height-120,False,'unmute',100,100))
                        background_sound.play()
                        unmute=True
                        mute=False
        if keyy[pygame.K_ESCAPE]:
            if help:
                help=False
                for settng in self.setting.sprites():
                    settng.kill()
                self.setting.add(Enmey((screen_width/2)-50,350,False,arrow,30,30))
            if choose_ship:
                choose_ship=False
                for settng in self.setting.sprites():
                    settng.kill()
                self.setting.add(Enmey((screen_width/2)-50,400,False,arrow,30,30))
    def draw(self):
        global count,play_color,help_color,ship_color,exit_color,retry_color,play_pos,help_pos,ship_pos,exit_pos,retry_pos
        for setting in self.setting.sprites():
            if setting.rect.y==250:
                play_color,help_color,ship_color,exit_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0) 
                play_pos,help_pos,ship_pos,exit_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2
                retry_pos=(screen_width/2)+10
                retry_color=(255,0,0)
            elif setting.rect.y==300:
                retry_color,help_color,ship_color,exit_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0)
                play_color=(255,0,0)
                play_pos=(screen_width/2)+10
                help_pos,ship_pos,exit_pos,retry_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2
            elif setting.rect.y==350:
                retry_color,play_color,ship_color,exit_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0)
                help_color=(255,0,0)
                help_pos=(screen_width/2)+10
                play_pos,ship_pos,exit_pos,retry_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2
            elif setting.rect.y==400:
                retry_color,play_color,help_color,exit_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0)
                ship_color=(255,0,0)
                ship_pos=(screen_width/2)+10
                play_pos,help_pos,exit_pos,retry_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2
            elif setting.rect.y==450:
                retry_color,play_color,help_color,ship_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0)
                exit_color=(255,0,0)
                exit_pos=(screen_width/2)+10
                play_pos,help_pos,ship_pos,retry_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2
            else:
                retry_color,play_color,help_color,ship_color,exit_color=(0,255,0),(0,255,0),(0,255,0),(0,255,0),(0,255,0)
                ship_pos,play_pos,help_pos,exit_pos,retry_pos=screen_width/2,screen_width/2,screen_width/2,screen_width/2,screen_width/2
        if help:
            screen.blit(font.render('press "a" to go left, "d" to go right and "space" to fire',True,(0,255,0)),(100,screen_height-60))
            self.setting.draw(screen)
            self.bullet.draw(screen)
            for bullet in self.bullet:
                if bullet.rect.y<0:
                    bullet.kill()
        elif choose_ship:
            self.setting.draw(screen)
            self.ship.draw(screen)
        else:
            if count!=0:
               screen.blit(font.render('retry',True,retry_color),(retry_pos,250)) 
            screen.blit(font.render('Play',True,play_color),(play_pos,300))
            screen.blit(font.render('help',True,help_color),(help_pos,350))
            screen.blit(font.render('ships',True,ship_color),(ship_pos,400))
            screen.blit(font.render('exit',True,exit_color),(exit_pos,450))
            self.setting.draw(screen)
            self.music.draw(screen)

setting_=Setting()

pygame.init()
pygame.display.set_caption('Space Invader')
pygame.display.set_icon(pygame.image.load('images/logo.jpg'))
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
        if event.type == ALIENLASER and shoot and in_game:
            if(life>0):
                game.enmey_shoot()
    if in_game:
        if wave_1 and num_enmeys==0:
            wave_1=False
            wave_2=True
            num_enmeys=20
            count-=1
        elif wave_2 and num_enmeys==0:
            wave_2=False
            wave_3=True
            num_enmeys=23
            count-=1
        elif wave_3 and num_enmeys==0:
            wave_3=False
            wave_4=True
            num_enmeys=30
            count-=1
        if count==0:
            game.add()
            count+=1
        if keys[pygame.K_SPACE] and in_game:
            if (current_time-time)>=800 and shoot:
                if(life>0):
                    game.player_shoot()
                    laser_sound.play()
                time=pygame.time.get_ticks()
        if keys[pygame.K_RSHIFT] and in_game and  current_time-recharge_time>=2000:
            recharge_time=pygame.time.get_ticks()
        if keys[pygame.K_ESCAPE] and in_game:
            in_game=False
        game.contact()
        game.player_move()
        if life>0:  
            game.enmey_move()
        game.shoot()
        #else:
            #screen.blit(text_surface, ((screen_width/2),0))
        game.draw()
    else:
        if setting_count==0:
            setting_.add()
            setting_count+=1
        setting_.draw()
        setting_.move()
        setting_.fun()
    pygame.display.flip()
    clock.tick(60)# fps
pygame.quit()                         