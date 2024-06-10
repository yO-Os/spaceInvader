import pygame
from random import choice
from player import Player
from enmey import Enmey
from bulet import BUllet
first_ship,second_ship=False,False
screen_height=700
screen_width=800
running=True
shoot=True
row=5
column=5
count=0
border1=0
life=3
border2=screen_width/2
time=pygame.time.get_ticks()
#  used to add game components and function to the game
class Game:

    global row ,column, screen,screen_width,screen_height,border2,border1,life
    def __init__(self):
        self.enmeys=pygame.sprite.Group()#  creates a group to add the enmey ship
        self.enmey_bulet=pygame.sprite.Group()#  creates a group to add the enmey bullet
        self.player=pygame.sprite.Group()#  creates a group to add the player ship
        self.player_bulet=pygame.sprite.Group()#  creates a group to add the player bullet
        #  bools that indicates the direction of the enmeys ship
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

        #the loop is used to access each object in the enmey group
        for alien in self.enmeys.sprites():

            #makes the enmey ship move to the right
            if self.right:
                    alien.rect.x += 1

            #makes the enmey ship move to the left
            elif self.left:
                    alien.rect.x -= 1

            #checkes if the ship in the most right ship reached the right of frame
            if alien.rect.right >= screen_width:
                 self.left=True
                 self.right=False

            #checkes if the ship in the most left ship reached the left of frame
            elif alien.rect.left <= 0:
                 self.left=False
                 self.right=True

            #kills the enmey ship that have been hit
            if (alien.hit):
                alien.kill()
#  moves the player ships
    def player_move(self):
        global first_ship,second_ship,shoot,border2,border1#imports global variable for use
        keys=pygame.key.get_pressed()#gets the key pressed from the keyboard

        #the loop is used to access each object in the player group
        for play in self.player.sprites():

            #checks if the player reached the left frame if it did't enables the ship to move to the left
            if keys[pygame.K_a] and play.rect.x-1>=0 and play.active and shoot:
                play.rect.x-=2

            #checks if the player reached the right frame if it did't enables the ship to move to the right
            elif keys[pygame.K_d] and play.rect.x+51<=screen_width and play.active and shoot:
                play.rect.x+=2

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
        if self.enmeys.sprites():
               random_alien = choice(self.enmeys.sprites())#chooses random enmey to shoot the bullets
               self.enmey_bulet.add(BUllet(random_alien.rect.center))#creates the bullet
#            
    def player_shoot(self):
        if self.player.sprites():

            #the loop is used to access each object in the player group
            for play in self.player.sprites():

                #checks if the player is on the field
                if play.active:              
                    self.player_bulet.add(BUllet((play.rect.center)))#creates the bullet
#  moves the bullets
    def shoot(self):
        global life

        #iterates through each enmey bullet
        for bullet in self.enmey_bulet.sprites():            
            bullet.rect.y+=9#  moves the bullets of the enmey

        #checks if the player have used all its life
            if life==0:
                bullet.kill()#distroies the enmeys bullet
        #iterates through each enmey bullet
        for bullet in self.player_bulet.sprites():
        #checks if the player have used all its life
            if life==0:
                bullet.kill()#distroies the players bullet
            bullet.rect.y-=9#  moves the bullets of the player
#   checks bullet contact  
    def contact(self):
        global shoot,life #imports global variable for use
        #iterates through the enmeys bullet
        for bullet in self.enmey_bulet.sprites():
            #iterates through the player group
            for play in self.player.sprites():
                if not(shoot):
                    bullet.kill()
                #iterates through each point of the enmey bullets height
                for height_bullet in range(bullet.rect.y,bullet.rect.y+16):
                    #iterates through each point of the player ships height
                    for height_player in range(play.rect.y,play.rect.y+50):
                        #checks if the bullet and the ship are on the same position vertically(y-axsis)
                        if height_bullet==height_player:
                            #iterates through each point of the enmey bullets width
                            for a in range(int(bullet.rect.x),int(bullet.rect.x+4)):
                                #iterates through each point of the player ships width
                                for b in range(int(play.rect.x),int(play.rect.x+50)):
                                    #checks if the bullet and the ship are on the same position horizontally(x-axsis)
                                    if a==b and play.active:
                                        life-=1
                                        play.hit=True
                                        play.active=False
                                        b+=(play.rect.x+51)
                                        a+=(bullet.rect.x+4)
                                        bullet.kill()
            #prevents the bullet from passing the wall
            if bullet.rect.y>=screen_height-68:
                bullet.kill()
        #does the same thing as the above loop but it checks if the enmey ship is hit
        for bullet in self.player_bulet.sprites():  
            for enmey in self.enmeys.sprites():
                for height_p_bullet in range(bullet.rect.y,bullet.rect.y+16):
                    for height_ship in range(enmey.rect.y,enmey.rect.y+50):
                        if height_p_bullet==height_ship:
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
        self.player.draw(screen)#displays the player ship
        self.enmeys.draw(screen)#displays the enmeys ship
        #displays the wall
        pygame.draw.rect(screen,'Grey',(border1,screen_height-68,screen_width/2,8))
        pygame.draw.rect(screen,'Grey',(border2,screen_height-68,screen_width/2,8))

        self.enmey_bulet.draw(screen)#displays the enmeys bullet
        self.player_bulet.draw(screen)#displays the players bullet
game=Game()
#my_font = pygame.font.SysFont('Noto Sans Display', 50)
#text_surface = my_font.render(str("Game over"), False, (255,255,255))
#screen init
pygame.init()
pygame.display.set_caption('Space Invader')
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
            if(life>0):
                game.enmey_shoot()
    if count==0:
        game.add()
        count+=1
    if keys[pygame.K_SPACE]:
        if (current_time-time)>=800 and shoot:
            if(life>0):
                game.player_shoot()
            time=pygame.time.get_ticks()
    if life>0:  
        game.contact()
        game.player_move()
        game.enmey_move()
        game.shoot()
    #else:
        #screen.blit(text_surface, ((screen_width/2),0))
    game.draw()
    pygame.display.flip()
    clock.tick(60)# fps
pygame.quit()                         