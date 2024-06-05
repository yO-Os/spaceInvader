import pygame
import random
screen_height=700
screen_width=800
running=True
left=True
right=False
count=0
count1= 0
e1=0
e2=0
e3=0
e4=0
e5=0
e6=0
num=0
num1=0
#screen init
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#classes
class ship():
    def __init__(self,x,y,hit):
        self.x=x
        self.y=y
        self.hit=hit
    def draw(self,window):
        pygame.draw.rect(window, (234,234,234), (self.x,self.y,25,25))
enm_01=ship(25,50,False)
enm_02=ship(60,50,False)
enm_03=ship(95,50,False)
enm_11=ship(47.5,80,False)
enm_12=ship(77.5,80,False)
enm_21=ship(60,110,False)
player=ship(screen_width/2,screen_height-50,False)
class shoot():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,window):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y,3,8))
bullet1=shoot(enm_01.x+12.5,enm_01.y+26)
bullet2=shoot(enm_02.x+12.5,enm_02.y+26)
bullet3=shoot(enm_03.x+12.5,enm_03.y+26)
bullet4=shoot(enm_11.x+12.5,enm_11.y+26)
bullet5=shoot(enm_12.x+12.5,enm_12.y+26)
bullet6=shoot(enm_21.x+12.5,enm_21.y+26)
bullet7=shoot(player.x+12.5,player.y-1)
def e_shoot():
    global bullet1
    global bullet2
    global bullet3
    global bullet4
    global bullet5
    global bullet6
    global enm_01
    global enm_02
    global enm_03
    global enm_11
    global enm_12
    global enm_21
    bullet1.y=enm_01.y+26
    bullet2.y=enm_02.y+26
    bullet3.y=enm_03.y+26
    bullet4.y=enm_11.y+26
    bullet5.y=enm_12.y+26
    bullet6.y=enm_21.y+26

    bullet1.x=enm_01.x+12.5
    bullet2.x=enm_02.x+12.5
    bullet3.x=enm_03.x+12.5
    bullet4.x=enm_11.x+12.5
    bullet5.x=enm_12.x+12.5
    bullet6.x=enm_21.x+12.5
    number=int(random.random()*5)+1
    if number==6 and not(enm_01.hit):
        bullet1.draw(screen)
    elif number==5 and not(enm_02.hit):
        bullet2.draw(screen)
    elif number==4 and not(enm_03.hit):
        bullet3.draw(screen)
    elif number==3 and not(enm_11.hit):
        bullet4.draw(screen)
    elif number==2 and not(enm_12.hit):
        bullet5.draw(screen)
    elif number==1 and not(enm_21.hit):
        bullet6.draw(screen)
    return number
def P_shoot():
    global bullet7
    global num1
    global count1
    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE] and (bullet7.y<=0 or count1==0) and not(player.hit):
        bullet7.x=player.x+12.5
        bullet7.y=player.y-1
        bullet7.draw(screen)
        num1=1
        count1+=1
    else:
        num1=0
    if bullet7.y<=0:
        bullet7.x=screen_width-9
    return num1
def move():
    global enm_01
    global enm_02
    global enm_03
    global enm_11
    global enm_12
    global enm_21
    global left
    global right
    if left and (enm_01.x-1)>0:
        enm_01.x-=1
        enm_02.x-=1
        enm_03.x-=1
        enm_11.x-=1
        enm_12.x-=1
        enm_21.x-=1
    elif right and (enm_03.x+26)<screen_width:
        enm_01.x+=1
        enm_02.x+=1
        enm_03.x+=1
        enm_11.x+=1
        enm_12.x+=1
        enm_21.x+=1
    if (enm_01.x-1<=0):
        left=False
        right=True
    elif (enm_03.x+26>=screen_width):
        left=True
        right=False
def p_m():
    global player
    key=pygame.key.get_pressed()
    if key[pygame.K_a] and (player.x-1)>0:
        player.x-=1
    elif key[pygame.K_d] and (player.x+26)< screen_width:
        player.x+=1
def contact(b_x,b_y,s_x,s_y):
    for x in range(int(b_x),int(b_x+3)):
        for y in range (int(s_x),int(s_x+25)):
            if(x==y and b_y>=s_y):
                print("contact")
                y+=(s_x+26)
                x+=b_x+4
                return True
        if(x==b_x+3):
            print("no contact")
            return False

#game loop
while running:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            running=False
    
    if(enm_01.hit and e1==0):
        bullet7.x=screen_width-9
        e1+=1
    elif(enm_02.hit and e2==0):
        bullet7.x=screen_width-9
        e2+=1
    elif(enm_03.hit and e3==0):
        bullet7.x=screen_width-9
        e3+=1
    elif(enm_11.hit and e4==0):
        bullet7.x=screen_width-9
        e4+=1
    elif(enm_12.hit and e5==0):
        bullet7.x=screen_width-9
        e5+=1
    elif(enm_21.hit and e6==0):
        bullet7.x=screen_width-9
        e6+=1 
    
    
    if(not(enm_01.hit)):
        enm_01.draw(screen)
        enm_01.hit=contact(bullet7.x,bullet7.y,enm_01.x,enm_01.y)
    if(not(enm_02.hit)):
        enm_02.draw(screen)
        enm_02.hit=contact(bullet7.x,bullet7.y,enm_02.x,enm_02.y)
    if(not(enm_03.hit)):
        enm_03.draw(screen)
        enm_03.hit=contact(bullet7.x,bullet7.y,enm_03.x,enm_03.y)
    if(not(enm_11.hit)):
        enm_11.draw(screen)
        enm_11.hit=contact(bullet7.x, bullet7.y, enm_11.x, enm_11.y)
    if(not(enm_12.hit)):
        enm_12.draw(screen)
        enm_12.hit=contact(bullet7.x, bullet7.y, enm_12.x, enm_12.y)
    if(not(enm_21.hit)):
        enm_21.draw(screen)
        enm_21.hit=contact(bullet7.x,bullet7.y, enm_21.x, enm_21.y)
    if(not(player.hit)):
        player.draw(screen)
        if contact(bullet1.x, bullet1.y, player.x, player.y):
           player.hit=True
        elif contact(bullet2.x, bullet2.y, player.x, player.y):
           player.hit=True
        elif contact(bullet3.x, bullet3.y, player.x, player.y):
           player.hit=True
        elif contact(bullet4.x, bullet4.y, player.x, player.y):
           player.hit=True
        elif contact(bullet5.x, bullet5.y, player.x, player.y):
           player.hit=True
        elif contact(bullet6.x, bullet6.y, player.x, player.y):
           player.hit=True
        else:
            player.hit=False      
    if (bullet1.y>=screen_height) or (bullet2.y>=screen_height) or(bullet3.y>=screen_height) or (bullet4.y>=screen_height) or (bullet5.y>=screen_height) or (bullet6.y>=screen_height or count==0):
       num= e_shoot()
    if num==6 and not(enm_01.hit):
        bullet1.y+=5
        bullet1.draw(screen)
    elif num==5 and not(enm_02.hit):
        bullet2.y+=5
        bullet2.draw(screen)
    elif num==4 and not(enm_03.hit):
        bullet3.y+=5
        bullet3.draw(screen)
    elif num==3 and not(enm_11.hit):
        bullet4.y+=5
        bullet4.draw(screen)
    elif num==2 and not(enm_12.hit):
        bullet5.y+=5
        bullet5.draw(screen)
    elif num==1 and not(enm_21.hit):
        bullet6.y+=5
        bullet6.draw(screen)
    if (P_shoot()==1 and not(player.hit)):      
        bullet7.y-=5
        bullet7.draw(screen)
    elif P_shoot()==0 and not(player.hit):
        bullet7.y-=5
        bullet7.draw(screen)
    count+=1
    move()
    p_m()
    pygame.display.flip()
    clock.tick(60)# fps
pygame.quit()