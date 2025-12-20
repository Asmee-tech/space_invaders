import pygame
from pygame.locals import*
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen=pygame.display.set_mode((700,600))
pygame.display.set_caption("Space invaders")
fonth=(255,255,255)
result=(99, 255, 51)
border=(255,255,255)
#font styles
hfont=pygame.font.SysFont("lemon drop",30)
wfont=pygame.font.SysFont("antrokas",50)
#game constants
fps=60
speeds=2
speedb=7
maxb=3
#loading the spaceships
red=pygame.image.load("spaceship_red.png")
blue=pygame.image.load("spaceship_blue.png")
bg=pygame.image.load("galaxy_bg.jpg")
bg=pygame.transform.scale(bg,(700,600))
red=pygame.transform.scale(red,(60,60))
blue=pygame.transform.scale(blue,(60,60))
#drawing border
bor=pygame.Rect(350,0,5,600)
#varieble for health
blueh=10
redh=10
#class for spaceship
class ss(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        super().__init__()
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    #function for vertical movement
    def vm(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 or self.rect.bottom>=600:
            self.rect.move_ip(0,-speed)
    #function for horizontal movement
    def hm(self,speed,p):
        self.rect.move_ip(speed,0)
        #p1=red
        if p==1:
            if self.rect.left<=0 or self.rect.right>=bor.left:
                self.rect.move_ip(-speed,0)
        #p2=blue
        if p==2:
            if self.rect.right>=700 or self.rect.left<=bor.right:
                self.rect.move_ip(-speed,0)
#creating the spaceship objects
rso=ss(red,100,300)
bso=ss(blue,550,300)
ssg=pygame.sprite.Group()
ssg.add(rso)
ssg.add(bso)
#while loop
run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
    keyp=pygame.key.get_pressed()
    #red movement
    if keyp[K_w]:
        rso.vm(-speeds)
    if keyp[K_a]:
        rso.hm(-speeds,1)
    if keyp[K_s]:
        rso.vm(speeds)
    if keyp[K_d]:
        rso.hm(speeds,1)
    #blue movement
    if keyp[K_UP]:
        bso.vm(-speeds)
    if keyp[K_LEFT]:
        bso.hm(-speeds,2)
    if keyp[K_DOWN]:
        bso.vm(speeds)
    if keyp[K_RIGHT]:
        bso.hm(speeds,2)
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,"white",bor)
    #screen.blit(bor,())
    redht=hfont.render("HEALTH:"+str(redh),1,fonth)
    blueht=hfont.render("HEALTH:"+str(blueh),1,fonth)
    screen.blit(redht,(10,20))
    screen.blit(blueht,(570,20))
    ssg.draw(screen)
    pygame.display.update()
pygame.quit()
