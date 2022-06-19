from pygame import *
from random import *
from math import *
import os
init()
os.environ["SDL_VIDEO_WINDOW_POS"]="300,250"
size=width,height=800,600
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

stad1=image.load("stadium1.jpg")
stadium1=transform.smoothscale(stad1,(800,600))
screen.blit(stadium1,(0,0))

plat1=Rect(200,210,110,10)
draw.rect(screen,GREEN,plat1)

plat2=Rect(490,210,110,10)
draw.rect(screen,GREEN,plat2)

plat3=Rect(70,360,660,10)
draw.rect(screen,GREEN,plat3)

myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False


    myclock.tick(60)
                       
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()

    
    display.flip()
quit()
