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
speeds=10
speedb=7
maxb=3
#loading the spaceships
red=pygame.image.load("spaceship_red.png")
blue=pygame.image.load("spaceship_blue.png")
bg=pygame.image.load("galaxy_bg.jpg")
bg=pygame.transform.scale(bg,(700,600))
red=pygame.transform.scale(red,(30,30))
blue=pygame.transform.scale(blue,(30,30))
#varieble for health
blueh=10
redh=10
#while loop
run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
    screen.blit(bg,(0,0))
    redht=hfont.render("HEALTH:"+str(redh),1,fonth)
    blueht=hfont.render("HEALTH:"+str(blueh),1,fonth)
    screen.blit(redht,(10,20))
    screen.blit(blueht,(600,20))
    pygame.display.update()
pygame.quit()