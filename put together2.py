from pygame import *
from random import *
from math import *
import os
init()
os.environ["SDL_VIDEO_WINDOW_POS"]="300,250"
size=width,height=800,600
screen=display.set_mode(size)
screen_res=(800,600)

GREY=(105,105,105)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW=(255,255,0)
WHITE = (255, 255, 255)
PINK=(255,0,255)

Character=["Unchosen","Unchosen"] 
char=["Mario","Mario"] 
movel=[6,6] 
mover=[12,12] 
lobby=False 
confirm=[False,False] 
stadium=("Unchosen") #Determines which stadium is choosen
cond=False 

mariocoords=Rect(100,100,90,82) #character choosing
luigicoords=Rect(190,100,83,82)
soniccoords=Rect(273,100,88,82)
bowsercoords=Rect(361,100,86,82)
bowserjcoords=Rect(446,100,83,82)
yoshicoords=Rect(532,100,83,82) 
randomcoords=Rect(605,100,83,82)
confirmcoords1=Rect(100,330,304,48)
confirmcoords2=Rect(406,330,292,48)
playgamecoords=(300,100,200,80)
stadium1coords=Rect(75,37.5,287.5,150)
stadium2coords=Rect(437.5,37.5,287.5,150)
stadium3coords=Rect(75,412.5,287.5,150)
stadium4coords=Rect(437.5,412.5,287.5,150)
stadium5coords=Rect(256.25,225,287,150)
playervscompcoords=Rect(50,100,200,100)
playervsplayercoords=Rect(550,100,200,100)
restartRect=Rect(300,100,200,50)
marioFont=font.Font("assets/SmashFont.ttf",108)
marioFontsmall=font.Font("assets/SmashFont.ttf",60)
marioFontsmall2=font.Font("assets/SmashFont.ttf",50)
playerfont=font.Font("assets/playerFont.ttf",20)
stadium1=image.load("pictures/stadium1.jpg")
stadium2=image.load("pictures/stadium2.jpg")
stadium3=image.load("pictures/stadium3.png")
stadium4=image.load("pictures/stadium4.png")
stadium5=image.load("pictures/stadium5.jpg")
marioandluigi=image.load("pictures/marioandluigi.png")
display.set_caption("Super Mario Smash Bros.")
mariostanding=image.load("pictures/mariostanding3.png")
luigistanding=image.load("pictures/luigistanding.png")
sonicstanding=image.load("pictures/sonicstanding.png")
bowserstanding=image.load("pictures/bowserstanding.png")
bowserjrstanding=image.load("pictures/bowserjrstanding.png")
yoshistanding=image.load("pictures/yoshistanding.png")
display.set_icon(image.load("pictures/windowpic.png"))
mapbackground=image.load("pictures/mapbackground.jpg")
characterbackground=image.load("pictures/charbackground.jpg")
characterchoose=image.load("pictures/characterseditedv4.png")
mapbackground=transform.smoothscale(mapbackground, (screen_res))
characterbackground=transform.smoothscale(characterbackground, (screen_res))
choosemodepic=image.load("pictures/playerchoosing.jpg")
comicFont = font.SysFont("Comic Sans MS", 15)
restart=marioFont.render("Restart",True,WHITE)
REstart=transform.smoothscale(restart,(200,50))

mixer.music.load("music/menu.mp3")
mixer.pre_init(44100,16,2,4096)
init()
jumpSound=mixer.Sound("sounds/jump.wav")
attack1Sound=mixer.Sound("sounds/attack1.wav")
attack2Sound=mixer.Sound("sounds/attack2.wav")
attack3Sound=mixer.Sound("sounds/attack3.wav")
opponent=False #if you chose computer or p2
attack=[[0,False,False,False],[0,False,False,False]]#ball attack, fall attack, close attack, block
click=[False,False] #If ball attack is used
right=[4,4]  
left=[4,4]  #counter for ball attack facing left
x=0   #x value
y=1   #y value
vy=2    
ground=3   
direction=4    
multiplier=5   #used for knock back
score=6   
pp2=False   #if there is p2
ai=False     #if there is a computer
direct=["",""]  #used in ball attack so ball will move in a straight line if you turn the character
stop=[0,0]     #counter for block
player=[[300,250,0,True,"right",0,0],[600,250,0,True,"right",0,0]] #player 1 and 2
computer=[600,319,0,True,"right",0,0] #AI/Computer
frame1=0
frame2=0 
move1=0 
move2=0 
bx=[[],[]]  #x value used for block so you stay in place

#__________stadiums___________________________
stad1=image.load("stadium1.jpg")
stadium1x=transform.smoothscale(stad1,(800,600))
stad2=image.load("stadium2.jpg")
stadium2x=transform.smoothscale(stad2,(800,600))
stad3=image.load("stadium3.png")
stadium3x=transform.smoothscale(stad3,(800,600))
stad4=image.load("stadium4.png")
stadium4x=transform.smoothscale(stad4,(800,600))
stad5=image.load("stadium5.jpg")
stadium5x=transform.smoothscale(stad5,(800,600))


#___________________________platforms________________________________
plat1Y=319 #coordinates for platforms for the stadiums
ground1Y=319
plat11=Rect(200,210,110,10)
plat12=Rect(490,210,110,10)
plat13=Rect(72,355,656,10)
plat14=Rect(0,0,0,0)

plat2Y=414
ground2Y=414
plat21=Rect(235,232,165,10)
plat22=Rect(490,300,185,10)
plat23=Rect(135,337,170,10)
plat24=Rect(48,450,705,10)


plat3Y=274
plat31=Rect(320,95,165,10)
plat32=Rect(503,203,170,10)
plat33=Rect(133,203,170,10)
plat34=Rect(48,310,705,10)

plat4Y=389
plat41=Rect(325,185,135,10)
plat42=Rect(500,300,110,10)
plat43=Rect(180,300,105,10)
plat44=Rect(125,425,535,10)

plat5Y=429
plat51=Rect(80,333,140,10)
plat52=Rect(590,333,130,10)
plat53=Rect(110,465,590,10)
plat54=Rect(0,0,0,0)

stadiumx=stadium1x
platY=plat1Y
plat1=plat11
plat2=plat12
plat3=plat13
plat4=plat14

def Game():
    global cond, stadium, platY, plat1, plat2, plat3, plat4, stadiumx, platY, Character, char, ai,pp2,n, move1, mover, opponent
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        #MOUSE CONTROLS
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.blit(choosemodepic,(0,0))
        draw.rect(screen,RED,playervscompcoords,2)
        draw.rect(screen,RED,playervsplayercoords,2)
        playervsaitext=playerfont.render(" PLAYER",False, WHITE) #Player vs Computer
        playervsaitext2=playerfont.render("   VS   ",False, WHITE)
        playervsaitext3=playerfont.render("COMPUTER",False, WHITE)
        playervsplayertext=playerfont.render(" PLAYER",False,WHITE) #Player vs Player
        playervsplayertext2=playerfont.render("   VS  ",False,WHITE)
        playervsplayertext3=playerfont.render(" PLAYER",False,WHITE)
        screen.blit(playervsaitext,(70,110))
        screen.blit(playervsaitext2,(70,140))
        screen.blit(playervsaitext3,(70,170))
        screen.blit(playervsplayertext,(570,110))
        screen.blit(playervsplayertext2,(570,140))
        screen.blit(playervsplayertext3,(570,170))
        if playervscompcoords.collidepoint(mx,my) and mb[0]==1 or playervsplayercoords.collidepoint(mx,my) and mb[0]==1: #If clicked on player vs player or player vs computer
            if playervscompcoords.collidepoint(mx,my) and mb[0]==1 and opponent==False:   #opponent is needed so you cant switch between computer and p2 after you picked one
                ai=True 
                pp2=False #player 2
                opponent=True #helps with bug
            if playervsplayercoords.collidepoint(mx,my) and mb[0]==1 and opponent==False:
                pp2=True
                ai=False #computer
                opponent=True
            cond=True #help with bug
        if ai==True:
            n=computer #what opponent you are playing against
            pp2=False
            bx=[player[0][x],n[x]]
        if pp2==True:
            n=player[1]
            ai=False
            bx=[player[0][x],n[x]]
        if cond:
            
        
        
            screen.blit(characterbackground, (0,0))
            screen.blit(characterchoose, (100,100))
            lobby=True
            draw.rect(screen,(BLACK),(30,300,200,290),3) #Character boxes
            draw.rect(screen,(BLACK),(570,300,200,290),3)
            draw.rect(screen,(BLACK),(30,270,200,30)) #Filled boxes (TEMP)
            draw.rect(screen,(BLACK),(570,270,200,30))
        
            p1title=playerfont.render("PLAYER 1",False, WHITE) #Titles ontop of character choosen boxes
            p2title=playerfont.render("PLAYER 2",False, WHITE)
            screen.blit(p1title,(50,280))
            screen.blit(p2title,(590,280))

       
            confirmtext=playerfont.render("CONFIRM",False,YELLOW) #Texts for the box above characters to confirm
            confirmtext2=playerfont.render("CONFIRM",False,PINK)

            if mb[0]==1 and confirm[0]==False:  #Player 1 - Indicates character choosen when clicked
                if mariocoords.collidepoint(mx, my):
                    Character[0]=("Mario") #Character chosen
                elif luigicoords.collidepoint(mx, my):
                    Character[0]=("Luigi")
                elif soniccoords.collidepoint(mx, my):
                    Character[0]=("Sonic")
                elif bowsercoords.collidepoint(mx, my):
                    Character[0]=("Bowser")
                elif bowserjcoords.collidepoint(mx, my):
                    Character[0]=("Bowser Jr.")
                elif yoshicoords.collidepoint(mx, my):
                    Character[0]=("Yoshi")
                elif randomcoords.collidepoint(mx, my):     
                    randchar=randint(0,5) #For the random chooser
                    if randchar==(0):
                        Character[0]=("Mario")
                    if randchar==(1):
                        Character[0]=("Luigi")
                    if randchar==(2):
                        Character[0]=("Sonic")
                    if randchar==(3):
                        Character[0]=("Bowser")
                    if randchar==(4):
                        Character[0]=("Bowser Jr.")
                    if randchar==(5):
                        Character[0]=("Yoshi")
        
            if lobby==True and confirm[0]==False: #PLAYER 1, character isnt confirmed
                if Character[0]=="Mario": #Indicates Character choosen
                    char[0]="mario"         #char is needed for sprites
                    movel[0]=6              
                    mover[0]=12             
                    draw.rect(screen,(RED),mariocoords,1) #Draws box around character choosen
                    screen.blit(mariostanding,(-35,410)) #Draws picture of character in box
                if Character[0]=="Luigi":
                    char[0]="luigi"
                    movel[0]=6
                    mover[0]=12
                    screen.blit(luigistanding,(75,410))
                    draw.rect(screen,(RED),luigicoords,1)
                if Character[0]==("Sonic"):
                    char[0]="sonic"
                    movel[0]=8
                    mover[0]=16
                    screen.blit(sonicstanding,(70,410))
                    draw.rect(screen,(RED),soniccoords,1)
                if Character[0]==("Bowser"):
                    char[0]="bowser"
                    movel[0]=6
                    mover[0]=12
                    screen.blit(bowserstanding,(40,420))
                    draw.rect(screen,(RED),bowsercoords,1)
                if Character[0]==("Bowser Jr."):
                    char[0]="minibowser"
                    movel[0]=4
                    mover[0]=8
                    screen.blit(bowserjrstanding,(40,407))
                    draw.rect(screen,(RED),bowserjcoords,1)
                if Character[0]==("Yoshi"):
                    char[0]="yoshi"
                    movel[0]=6
                    mover[0]=12
                    screen.blit(yoshistanding,(60,410))
                    draw.rect(screen,(RED),yoshicoords,1)
                if Character[0]==("Rand"):
                    draw.rect(screen,(RED),randomcoords,1)
                if Character[0]!=("Unchosen"):
                    draw.rect(screen,(255,0,255),confirmcoords1) #Confirm box, to confirm your choice
                    screen.blit(confirmtext,(180,345))
                if confirmcoords1.collidepoint(mx,my) and mb[0]==1: 
                    confirm[0]=True
            
            if confirm[0] and not confirm[1]:
                if Character[0]=="Mario": #Indicates Character choosen
                    char[0]="Mario"
                    movel[0]=6
                    mover[0]=12
                    draw.rect(screen,(RED),mariocoords,1) #Draws box around character choosen
                    screen.blit(mariostanding,(-35,410)) #Draws picture of character in box
                if Character[0]=="Luigi":
                    char[0]="luigi"
                    movel[0]=6
                    mover[0]=12
                    screen.blit(luigistanding,(75,410))
                    draw.rect(screen,(RED),luigicoords,1)
                if Character[0]==("Sonic"):
                    char[0]="sonic"
                    movel[0]=8
                    mover[0]=16
                    screen.blit(sonicstanding,(70,410))
                    draw.rect(screen,(RED),soniccoords,1)
                if Character[0]==("Bowser"):
                    char[0]="bowser"
                    movel[0]=6
                    mover[0]=12
                    screen.blit(bowserstanding,(40,420))
                    draw.rect(screen,(RED),bowsercoords,1)
                if Character[0]==("Bowser Jr."):
                    char[0]="minibowser"
                    movel[0]=4
                    mover[0]=8
                    screen.blit(bowserjrstanding,(40,407))
                    draw.rect(screen,(RED),bowserjcoords,1)
                if Character[0]==("Yoshi"):
                    char[0]="yoshi"
                    movel[0]=6 
                    mover[0]=12 
                    screen.blit(yoshistanding,(60,410))
                    draw.rect(screen,(RED),yoshicoords,1)
                if Character[0]==("Rand"):
                    draw.rect(screen,(RED),randomcoords,1)
            
                        
                                                
                        
            if lobby==True and confirm[0]==True: #Player 2- Player 1 is now confirmed but Player 2 isnt
                if Character[1]==("Mario"): #Indicates character choosen
                    draw.rect(screen,(YELLOW),mariocoords,1) #Draws box around player choosen in YELLOW
                    screen.blit(mariostanding,(510,410)) #Draws picture of player choosen in box
                if Character[1]==("Luigi"):
                    draw.rect(screen,(YELLOW),luigicoords,1)
                    screen.blit(luigistanding,(620,410))
                if Character[1]==("Sonic"):
                    draw.rect(screen,(YELLOW),soniccoords,1)
                    screen.blit(sonicstanding,(620,410))
                if Character[1]==("Bowser"):
                    draw.rect(screen,(YELLOW),bowsercoords,1)
                    screen.blit(bowserstanding,(580,420))
                if Character[1]==("Bowser Jr."):
                    draw.rect(screen,(YELLOW),bowserjcoords,1)
                    screen.blit(bowserjrstanding,(580,410))
                if Character[1]==("Yoshi"):
                    draw.rect(screen,(YELLOW),yoshicoords,1)
                    screen.blit(yoshistanding,(610,410))
                if Character[1]==("Rand"):
                    draw.rect(screen,(YELLOW),randomcoords,1)
                if Character[1]!=("Unchosen"):
                    draw.rect(screen,(YELLOW),confirmcoords2)
                    screen.blit(confirmtext2,(480,345))
                if confirmcoords2.collidepoint(mx,my) and mb[0]==1: #To Confirm
                        confirm[1]=True

            
            if mb[0]==1 and confirm[0]==True and confirm[1]==False: #Player 2 - Indicates character choosen when clicked
                if mariocoords.collidepoint(mx, my):
                    Character[1]=("Mario")
                    char[1]="Mario" #player 2 character
                    movel[1]=6 #move left
                    mover[1]=12 #move right
                elif luigicoords.collidepoint(mx, my):
                    Character[1]=("Luigi")
                    char[1]="luigi"
                    movel[1]=6
                    mover[1]=12
                elif soniccoords.collidepoint(mx, my):
                    Character[1]=("Sonic")
                    char[1]="sonic"
                    movel[1]=8
                    mover[1]=16
                elif bowsercoords.collidepoint(mx, my):
                    Character[1]=("Bowser")
                    char[1]="bowser"
                    movel[1]=6
                    mover[1]=12
                elif bowserjcoords.collidepoint(mx, my):
                    Character[1]=("Bowser Jr.")
                    char[1]="minibowser"
                    movel[1]=4
                    mover[1]=8
                elif yoshicoords.collidepoint(mx, my):
                    Character[1]=("Yoshi")
                    char[1]="yoshi"
                    movel[1]=6
                    mover[1]=12
                elif randomcoords.collidepoint(mx, my):
                    randchar=randint(0,5) #For random chooser
                    if randchar==(0):
                        Character[1]=("Mario")
                        char[1]="Mario"
                    if randchar==(1):
                        Character[1]=("Luigi")
                        char[1]="luigi"
                    if randchar==(2):
                        Character[1]=("Sonic")
                        char[1]="sonic"
                    if randchar==(3):
                        Character[1]=("Bowser")
                        char[1]="bowser"
                    if randchar==(4):
                        Character[1]=("Bowser Jr.")
                        char[1]="minibowser"
                    if randchar==(5):
                        Character[1]=("Yoshi")
                        char[1]="yoshi"
            if confirm[0]==True and confirm[1]==True: #When both players confirmed
                screen.blit(mapbackground, (0,0)) 
                draw.rect(screen,BLACK,stadium1coords,2)
                draw.rect(screen,BLACK,stadium2coords,2)
                draw.rect(screen,BLACK,stadium3coords,2)
                draw.rect(screen,BLACK,stadium4coords,2)
                draw.rect(screen,BLACK,stadium5coords,2)
                maptext=playerfont.render("CHOOSE A MAP",False, WHITE)
                screen.blit(maptext,(280,10))
                screen.blit(stadium1,stadium1coords)
                screen.blit(stadium2,stadium2coords)
                screen.blit(stadium3,stadium3coords)
                screen.blit(stadium4,stadium4coords)
                screen.blit(stadium5,stadium5coords)

                if stadium1coords.collidepoint(mx,my) and mb[0]==1: #Maps
                    draw.rect(screen,RED,stadium1coords,5)
                    stadium=("1") #stadium
                    mixer.music.load("music/stadium1.mp3")
                if stadium2coords.collidepoint(mx,my) and mb[0]==1:
                    draw.rect(screen,RED,stadium2coords,5)
                    stadium=("2")
                if stadium3coords.collidepoint(mx,my) and mb[0]==1:
                    draw.rect(screen,RED,stadium3coords,5)
                    stadium=("3")
                if stadium4coords.collidepoint(mx,my) and mb[0]==1:
                    draw.rect(screen,RED,stadium4coords,5)
                    stadium=("4")
                if stadium5coords.collidepoint(mx,my) and mb[0]==1:
                    draw.rect(screen,RED,stadium5coords,5)
                    stadium=("5")
                if stadium==("1"):
                    stadiumx=stadium1x
                    platY=plat1Y
                    plat1=plat11
                    plat2=plat12
                    plat3=plat13
                    plat4=plat14
                if stadium==("2"):
                    stadiumx=stadium2x
                    platY=plat2Y
                    plat1=plat21
                    plat2=plat22
                    plat3=plat23
                    plat4=plat24
                if stadium==("3"):
                    stadiumx=stadium3x
                    platY=plat3Y
                    plat1=plat31
                    plat2=plat32
                    plat3=plat33
                    plat4=plat34
                if stadium==("4"):
                    stadiumx=stadium4x
                    platY=plat4Y
                    plat1=plat41
                    plat2=plat42
                    plat3=plat43
                    plat4=plat44
                if stadium==("5"):
                    stadiumx=stadium5x
                    platY=plat5Y
                    plat1=plat51
                    plat2=plat52
                    plat3=plat53
                    plat4=plat54
                if stadium!="Unchosen":
                    return "menu"
            
        keys = key.get_pressed()
        myClock.tick(50)
        display.flip()



def instructions():
    running = True
    
    inst = image.load("pictures/instructionback.png") #Background picture
    inst = transform.smoothscale(inst, screen.get_size())
    screen.blit(inst,(0,0))
    
    p1instruct=marioFont.render("PLAYER 1",False, BLUE) #INSTRUCTIONS!
    p1instruct2=playerfont.render("JUMP - W",False, BLACK)
    p1instruct3=playerfont.render("LEFT - A",False, BLACK)
    p1instruct4=playerfont.render("RIGHT - D",False, BLACK)
    p1instruct5=playerfont.render("DOWN ATTACK - S",False,BLACK)
    p1instruct6=playerfont.render("KEYPAD ON TOP",False, RED)
    p1instruct7=playerfont.render("0 - BALL ATTACK",False, BLACK)
    p1instruct8=playerfont.render("9 - BLOCK",False, BLACK)
    p1instruct9=playerfont.render("8 - CLOSE ATTACK",False, BLACK)
    p2instruct=marioFont.render("PLAYER 2",False,BLUE)
    p2instruct2=playerfont.render("JUMP - ARROW UP",False, BLACK)
    p2instruct3=playerfont.render("LEFT - ARROW LEFT",False, BLACK)
    p2instruct4=playerfont.render("RIGHT - ARROW RIGHT",False, BLACK)
    p2instruct5=playerfont.render("DOWN ATTACK - ARROW DOWN",False, BLACK)
    p2instruct6=playerfont.render("KEYPAD ON RIGHT",False, RED)
    p2instruct7=playerfont.render("0 - BALL ATTACK",False, BLACK)
    p2instruct8=playerfont.render("9 - BLOCK",False, BLACK)
    p2instruct9=playerfont.render("8 - CLOSE ATTACK",False, BLACK)
    
    screen.blit(p1instruct,(40,5)) #INSTRUCTIONS BLITTED ON SCREEN
    screen.blit(p1instruct2,(40,110))
    screen.blit(p1instruct3,(40,140))
    screen.blit(p1instruct4,(40,170))
    screen.blit(p1instruct5,(40,210))
    screen.blit(p1instruct6,(40,240))
    screen.blit(p1instruct7,(40,270))
    screen.blit(p1instruct8,(40,300))
    screen.blit(p1instruct9,(40,330))
    screen.blit(p2instruct,(400,5))
    screen.blit(p2instruct2,(400,110))
    screen.blit(p2instruct3,(400,140))
    screen.blit(p2instruct4,(400,170))
    screen.blit(p2instruct5,(400,210))
    screen.blit(p2instruct6,(400,240))
    screen.blit(p2instruct7,(400,270))
    screen.blit(p2instruct8,(400,300))
    screen.blit(p2instruct9,(400,330))
    screen.blit(marioandluigi,(300,400))
    
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False

        display.flip()
    return "menu"
        
def credit():
    running = True
    screen.fill(WHITE)
    credit1= image.load("pictures/credit1.jpg") #Credit Background
    credit1= transform.smoothscale(credit1,screen.get_size())
    screen.blit(credit1,(0,0))
    
    credititle=marioFont.render("CREDITS",False, BLUE) #Credit Texts and Names
    sajanfont=marioFontsmall.render("Sajan Flora", False, WHITE)
    sehajfont=marioFontsmall.render("Sehaj Cheema", False, RED)
    alexfont=marioFontsmall.render("Alex Stefanovski", False, GREEN)
     
    screen.blit(credititle,(70,0)) 
    screen.blit(sajanfont,(70,200))
    screen.blit(sehajfont,(70,350))
    screen.blit(alexfont,(70,500))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        display.flip()
    return "menu"

def close(): #NEED TO CHANGE TO QUIT/EXIT
    running = True
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"
        ax,ay = mouse.get_pos()
        ab = mouse.get_pressed()
        if ab[0] == 1 and Rect(320,520,160,60).collidepoint(ax,ay):
            quit()


def menu():
    running = True
    myClock = time.Clock()
    buttons=[Rect(320,310,160,60),Rect(320,380,160,60),Rect(320,450,160,60),Rect(320,520,160,60)] #BUTTONS FOR MENU
    playbutton=Rect(350,200,200,80)
    vals = ["game","instructions","credits","close"]
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        menupage=image.load("pictures/menubackground.jpg")
        menupage=transform.smoothscale(menupage,(screen_res))
        screen.blit(menupage,(0,0))
        
        title=image.load("pictures/titlepage3.png") #TITLE ON MENU
        screen.blit(title,(210,0))
        
        playfont=marioFontsmall.render("PLAY", False, BLUE) #TEXT ON BUTTONS
        creditfont=marioFontsmall2.render("instructions",False, BLUE)
        instructionfont=marioFontsmall.render("CREDITS",False, BLUE)
        quittext=marioFontsmall.render("QUIT",False,BLUE)
        
        for i in range(len(buttons)): #buttons
            draw.rect(screen,(RED),buttons[i])
            screen.blit(playfont,(370,310))
            screen.blit(creditfont,(320,380))
            screen.blit(instructionfont,(350,450))
            screen.blit(quittext,(370,520))
            if buttons[i].collidepoint(mx,my):
                draw.rect(screen,(0,255,0),buttons[i],2)
                if mb[0]==1:
                    return vals[i]
            else:
                draw.rect(screen,(255,255,0),buttons[i],2)
            
           
        display.flip()

#rec is player hitbox
def drawScene(screen,p1,p2,picList1,picList2,comp,attack,attack2):
    global direct, platY, plat1, plat2, plat3, plat4, stadiumx
    'this function is drawing 1 of the 24 pictures'
    rec1=Rect(p1[x],p1[y],17,37)
    rec2=Rect(n[x],n[y],17,37)

    draw.rect(screen,RED,plat1)
    draw.rect(screen,RED,plat2)
    draw.rect(screen,RED,plat3)    #platforms
    draw.rect(screen,RED,plat4)
    
    draw.rect(screen,RED,rec1,1)
    draw.rect(screen,RED,rec2,1)    #hit boxes
    screen.blit(stadiumx,(0,0))

    pic1=picList1[move1][int(frame1)]
    pic2=picList2[move2][int(frame2)]   #players
    screen.blit(pic1,(p1[x],p1[y]))
    screen.blit(pic2,(n[x],n[y]))

    score1=comicFont.render(str(p1[score]),True,BLACK)
    percent1=comicFont.render(str(p1[multiplier]),True,BLACK)#score and multiplier
    percentage=comicFont.render(("%"),True,BLACK)
    score2=comicFont.render(str(n[score]),True,BLACK)
    percent2=comicFont.render(str(n[multiplier]),True,BLACK)

    screen.blit(score2,(600,50))
    screen.blit(percent2,(550,50))
    screen.blit(percentage,(580,50))
    screen.blit(score1,(200,50))
    screen.blit(percent1,(250,50))
    screen.blit(percentage,(280,50))
    
#_________________________p1___________________________
    if click[0]==True:   #click is needed so you dont have to hold down 0 to perform the full attack
        if direct[0]=="left":
            if left[0]>=88:   #counter for ball
                left[0]=4   #starts at 4 so it looks like it starts infront of him
                attack[0]=0
                click[0]=False    #ends the attack
            attack[0]=p1[x]-left[0]
            draw.circle(screen,(255,0,0),(attack[0],int(p1[y]+8)),4)
            left[0]+=3
        if direct[0]=="right":
            if right[0]>=88:
                right[0]=4
                attack[0]=0
                click[0]=False
            attack[0]=p1[x]+right[0]
            draw.circle(screen,(255,0,0),(attack[0],int(p1[y]+8)),4)
            right[0]+=3

    if attack[3]==True and p1[direction]=="left":    #draws a circle around the player for block
        draw.circle(screen,(BLUE),(int(p1[x]),int(p1[y])+18),40,2)
    if attack[3]==True and p1[direction]=="right":
        draw.circle(screen,(BLUE),(int(p1[x]+4),int(p1[y])+18),40,2)

#_________________________p2 or computer____________________
    if click[1]==True:
        if direct[1]=="left":
            if left[1]>=88: #counter for the ball so it doseant go on forever
                left[1]=4
                attack2[0]=0
                click[1]=False
            attack2[0]=n[x]-left[1]
            draw.circle(screen,(255,0,255),(attack2[0],int(n[y]+8)),4)
            left[1]+=3
        if direct[1]=="right":
            if right[1]>=88:
                right[1]=4
                attack2[0]=0
                click[1]=False
            attack2[0]=n[x]+right[1]
            draw.circle(screen,(255,0,255),(attack2[0],int(n[y]+8)),4)
            right[1]+=3

    if attack2[3]==True and n[direction]=="left":    #block
        draw.circle(screen,(BLUE),(int(n[x]),int(n[y])+18),40,2)
    if attack2[3]==True and n[direction]=="right":
        draw.circle(screen,(BLUE),(int(n[x]+4),int(n[y])+18),40,2)
#___________________________winner___________________________________________
    if p1[score]==3:
        if ai==True:
            winner=marioFont.render("Computer Wins",True,BLUE)  #when the computer wins
            screen.blit(stadiumx,(0,0))
            screen.blit(winner,(200,200))
            draw.rect(screen,RED,(restartRect))
            screen.blit(REstart,(300,100))
        if pp2==True:
            winner=marioFont.render("Player 2 Wins",True,BLUE)   #when player 2 wins
            screen.blit(stadiumx,(0,0))
            screen.blit(winner,(200,200))
            draw.rect(screen,RED,(restartRect))
            screen.blit(REstart,(300,100))
    if n[score]==3:

        winner=marioFont.render("Player 1 Wins",True,BLUE)   #when p1 wins
        screen.blit(stadiumx,(0,0))
        screen.blit(winner,(200,200))
        draw.rect(screen,RED,(restartRect))
        screen.blit(REstart,(300,100))
            
    display.flip()

def Restart(p1):
    global n,player, stadium, Character, opponent, confirm
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    if p1[score]==3 or n[score]==3:    #you lose if you fall off 3 times
        if restartRect.collidepoint(mx,my) and mb[0]==1:
            stadium=("Unchosen")
            opponent=False
            confirm[0],confirm[1]=False,False
            lobby=False
            Character[0],Character[1]=("Unchosen"),("Unchosen")
            p1[score],n[score]=0,0
            p1[multiplier],n[multiplier]=0,0
            n[x],p1[x]=600,200
            n[y],p1[y]=250,250 #resets everything so you can play again
            page="menu"
            return menu
    
def P1(p1,p2,attack):
    global move1,frame1
    rec=Rect(p1[x],p1[y],20,37)
    keys=key.get_pressed()

    newMove1=-1
    if keys[K_d] and attack[3]==False:
        newMove1=0
        p1[x]+=4        #adding moves to the right
        p1[direction]="right" 
        bx[0]=p1[x]
    if keys[K_a] and attack[3]==False:
        newMove1=1
        p1[x]-=4        #subtratcing moves to the left
        p1[direction]="left"
        bx[0]=p1[x]

    if keys[K_w] and p1[ground]==True and attack[3]==False:  #cant move while using block
        jumpSound.play()  #jump sound effect
        p1[vy]-=17
        p1[ground]=False        
    p1[y]+=p1[vy]   #adding gravity to y value

    
    if p1[y]>=600 and p1[vy]<44:  #when pq falls off the platform
        p1[x]=300
        p1[y]=250
        p1[vy]=0
        p1[multiplier]=0
        p1[ground]=True
        p1[score]+=1
    elif p1[y]>platY and p1[vy]<30 and p1[vy]>-30:
        if rec.colliderect(plat4):
            p1[y]=platY
    p1[vy]+=0.8   #increasing gravity


    if keys[K_a] and keys[K_d]:
        frame1=0          #if u press both at the same time it goes to the first postion

    if keys[K_a]==False and keys[K_d]==False:
        frame1=0

    if move1==newMove1:  #new move was selected
        frame1+=0.2
        if frame1>=len(pics1[move1]):
            frame1=1
    elif newMove1!=-1:#move was selected
        move1=newMove1
        frame1=1


def P2(p2,p1, attack2):
    global move2,frame2
    keys=key.get_pressed()
    if pp2==True:

        rec2=Rect(n[x],n[y],20,37)  #hit box
        newMove2=-1
        if keys[K_RIGHT]  and attack2[3]==False:  #cant move while using block
            newMove2=0
            n[x]+=4
            n[direction]="right"
            bx[1]=n[x]   #used to keep player in place during block
        if keys[K_LEFT]  and attack2[3]==False:
            newMove2=1
            n[x]-=4
            n[direction]="left"
            bx[1]=n[x]

        if keys[K_UP] and p2[ground]==True and attack2[3]==False:
            jumpSound.play()
            n[vy]-=17
            n[ground]=False        
        n[y]+=n[vy]

    
        if n[y]>=600:
            n[x]=600
            n[y]=250
            n[vy]=0                     #when you die
            n[multiplier]=0
            n[ground]=True
            n[score]+=1
  
        n[vy]+=0.8
   

        if keys[K_LEFT] and keys[K_RIGHT]:  
            frame2=0

        if keys[K_LEFT]==False and keys[K_RIGHT]==False:
            frame2=0

        if move2==newMove2:
            frame2+=0.2
            if frame2>=len(pics2[move2]):
                frame2=1
        elif newMove2!=-1:#move was selected
            move2=newMove2
            frame2=1

def AI(p1,comp,attack2):
    global move2,frame2
    
    if ai==True:
        newMove2=-1
        if p1[ground]==True and n[ground]==True and attack2[3]==False and p1[y]-n[y]>30: #so the computer doseant get stuck ontop of the platform
            n[x]+=4
            newMove2=0
            n[direction]="right"  #when to move right
            bx[1]=n[x]
        elif p1[x]-n[x]>0:
            if n[x]>74 and n[x]<720 and attack2[3]==False:
                n[x]+=4
                newMove2=0
                n[direction]="right"
                bx[1]=n[x]  #bx is used for block
        elif p1[x]-n[x]<=0:
            if n[x]<720 and n[x]>74  and attack2[3]==False:
                n[x]-=4     #when to move left
                newMove2=1
                n[direction]="left"
                bx[1]=n[x]    

        if n[x]<=72  and attack2[3]==False: #if in the boundaries and block is false
            n[x]+=4
            n[direction]="right"
            bx[1]=n[x]  #x value for block
            newMove2=1
        elif n[x]>=720  and attack2[3]==False: #if in the boundaries and block is false
            n[direction]="left"
            n[x]-=4
            newMove2=0
            bx[1]=n[x]  #x value for block

        if p1[y]<=platY-30 and n[ground]==True and attack2[3]==False:   #following p1 on to the platform
            if p1[x]>=210 and p1[x]<=platY or p1[x]>=490 and p1[x]<=600:
                jumpSound.play()  #jump sound effect
                n[vy]-=17
                n[ground]=False
        n[y]+=n[vy]
    
        if n[y]>=600:
            n[x]=600
            n[y]=250   #if u die
            n[vy]=0
            n[score]+=1
            n[multiplier]=0
            n[ground]=True
        n[vy]+=0.8
        
        if move2==newMove2:
            frame2+=0.2    #sprites
            if frame2>=len(pics2[move2]):
                frame2=1
        elif newMove2!=-1:#move was selected
            move2=newMove2
            frame2=1
    

#############################
def checkCollision(p1,p2,attack,attack2,comp):
    global platY, plat1, plat2, plat3, plat4, stadiumx
    rec=Rect(p1[x],p1[y],20,37)  #hit boxes
    rec2=Rect(n[x],n[y],20,37)
    if rec.colliderect(plat1):
        if p1[vy]>0:#falling down
            p1[ground]=True
            p1[vy]=0    #reset gravity because you are on the ground
            p1[y]=plat1.top-36#top finds the top Y of the rect

    elif rec.colliderect(plat2):
        if p1[vy]>0:
            p1[ground]=True
            p1[vy]=0
            p1[y]=plat2.top-36
            
    elif rec.colliderect(plat3):
        if p1[vy]>0:
            p1[ground]=True
            p1[vy]=0
            p1[y]=plat3.top-36

    elif rec.colliderect(plat4):
        if p1[vy]>0:#falling down
            p1[ground]=True
            p1[vy]=0
            p1[y]=plat4.top-36
      
    if rec2.colliderect(plat1):
        if n[vy]>0:
            n[ground]=True
            n[vy]=0
            n[y]=plat1.top-36#top finds the top Y of the rect

    elif rec2.colliderect(plat2):
        if n[vy]>0:
            n[ground]=True
            n[vy]=0
            n[y]=plat2.top-36
            
    elif rec2.colliderect(plat3):
        if n[vy]>0:
            n[ground]=True
            n[vy]=0
            n[y]=plat3.top-36

    elif rec2.colliderect(plat4):
        if n[vy]>0:
            n[ground]=True
            n[vy]=0
            n[y]=plat4.top-36

#############################
def attacks(p1,p2,attack,attack2,comp):
    global direct, stop
    rec=Rect(p1[x],p1[y],20,37)
    rec2=Rect(p2[x],p2[y],20,37)
    rec3=Rect(n[x],n[y],17,37)
    keys=key.get_pressed()

    if keys[K_0]:
        click[0]=True    #ball attack
        direct[0]=p1[direction]   
    elif keys[K_s]:
        if p1[ground]==False: #can only use fall attack when falling
            attack[1]=True   #fall attack
    elif keys[K_8]:
        attack[2]=True    #close attack
    elif keys[K_9] and p1[ground]==True:
        attack[3]=True   #block

    if pp2==True:    #if p2 is being usd
        if keys[K_KP0]:
            click[1]=True
            direct[1]=n[direction]
        if keys[K_DOWN]:
            if n[ground]==False:  #can only use fall attack when falling
                attack2[1]=True
        if keys[K_KP8]:
            attack2[2]=True   #close attack
        if keys[K_KP9] and n[ground]==True:  #can only use block whenn on the ground
            attack2[3]=True

    if ai==True:        #if computer is being used
        if n[y]+8>p1[y]-29 and n[y]+8<p1[y]+29:   #i want to be able to hit him on any part of the body
            if attack[0]-n[x]>0 and attack[0]-n[x]<10:  #if the ball attack is close enough use block
                if n[ground]==True:
                    attack2[3]=True
            elif attack[0]-n[x]<0 and attack[0]-n[x]>-10:  #if the ball attack is close enough use block
                if n[ground]==True:
                    attack2[3]==True
            elif p1[x]-n[x]>0 and p1[x]-n[x]<30:    #when to use the close attack
                attack2[2]=True
            elif p1[x]-n[x]>0 and p1[x]-n[x]<50:   #when to use the ball attack
                click[1]=True
                direct[1]=n[direction]
            elif p1[x]-n[x]<0 and p1[x]-n[x]>-50: #when to use the ball attack
                click[1]=True
                direct[1]=n[direction]
        elif n[y]<p1[y]:
            attack2[1]==True  #when to use fall hit attack, when the computer is above p1

#_____________________p1__________________________________________           

    if click[0]==True:
        attack1Sound.play()
        if attack[0]>n[x]-5 and attack[0]<n[x]+5:  #if the ball is in contact with the opponent
            if p1[y]+8>n[y]-29 and p1[y]+8<n[y]+29  and attack2[3]==False:    #if block is false
                if attack[0]-n[x]>0:  
                    if n[multiplier]<80:   #multilier needs to be higher then 200 so knockback isnt decreased
                        n[x]-=30   #knockback
                        n[y]-=15    #vertical knockback
                        n[multiplier]+=5   #increase the multiplier
                    else:
                        n[x]-=30*(n[multiplier]//80)   #when multiplier is above 200 so knock back increaes
                        n[multiplier]+=5
                        n[y]-=15    #vertical knockback
                    attack[0]=0
                elif attack[0]-n[x]<0:
                    if n[multiplier]<80  and attack2[3]==False:
                        n[x]+=30
                        n[multiplier]+=5
                        n[y]-=15  #vertical knockback
                    else:
                        n[x]+=30*(n[multiplier]//80)
                        n[multiplier]+=5
                        n[y]-=15
                    attack[0]=0
    if click[0]==False:   #so the opponent doseant get hit when there is no ball attack
        attack[0]=0
            
    if attack[1]==True and p1[y]>150:   #had to be >150 because if it was less there were a lot of bugs
        attack2Sound.play()  #sound effect
        p1[y]+=p1[vy]
        p1[vy]+=3
        if p1[y]==n[y]:#if they have the same y value
            if n[x]-p1[x]<=0 and n[x]-p1[x]>=-20  and attack2[3]==False:  #block has to equal false during other attacks   #to the left
                if n[multiplier]<=80:  #multiplier
                    n[x]-=50   
                    n[multiplier]+=20 #adding knockback
                    n[y]-=25 #vertical knockback
                else:
                    n[multiplier]+=20
                    n[x]-=50*(n[multiplier]//80)
                    n[y]-=25
            elif n[x]-p1[x]>0 and n[x]-p1[x]<=20  and attack2[3]==False:        #to the right
                if n[multiplier]<=80:
                    n[x]+=50
                    n[multiplier]+=20
                    n[y]-=25
                else:
                    n[multiplier]+=20
                    n[x]+=50*(n[multiplier]//80)
                    n[y]-=25
            attack[1]=False  #end the attack

    if attack[2]==True:
        attack3Sound.play()
        if p1[x]>n[x]-30 and p1[x]<n[x]+30:
            if p1[y]+8>n[y]-29 and p1[y]+8<n[y]+29 and attack2[3]==False:  #want to be able to hit any part of the opponent and block has to be false
                if p1[direction]=="left":
                    if n[multiplier]<80:
                        n[multiplier]+=15
                        n[x]-=15
                        n[y]-=15
                    else:
                        n[multiplier]+=15
                        n[x]-=15*(n[multiplier]//80)
                        n[y]-=15
                elif p1[direction]=="right":
                    if n[multiplier]<80:
                        n[x]+=15
                        n[multiplier]+=15
                        n[y]-=15
                    else:
                        n[multiplier]+=15
                        n[x]+=15*(n[multiplier]//80)
                        n[y]-=15
        attack[2]=False

    if attack[3]==True:#block
        if p1[ground]==True:  #has to be on the ground for block to work
            if stop[0]>=60:
                stop[0]=0
                attack[3]=False
            if stop[0]<60:
                stop[0]+=1
                p1[x]=bx[0]

#___________________________p2 or computer______________________________________  
    if click[1]==True:          #ball attack p2
        attack1Sound.play()     #ball attack sound
        if attack2[0]>p1[x]-5 and attack2[0]<p1[x]+5:   #
            if n[y]+8>p1[y]-29 and n[y]+8<p1[y]+29  and attack[3]==False:  #block has to equal false
                if attack2[0]-p1[x]>0:
                    if p1[multiplier]<80:
                        p1[x]-=30
                        p1[multiplier]+=5   #adding to multiplier
                        p1[y]-=15
                    else:
                        p1[x]-=30*(p1[multiplier]//80)
                        p1[multiplier]+=5
                        p1[y]-=15
                    attack2[0]=0  
                elif attack2[0]-p1[x]<0:
                    if p1[multiplier]<80:
                        p1[x]+=30
                        p1[multiplier]+=5
                        p1[y]-=15
                    else:
                        p1[x]+=30*(p1[multiplier]//80)
                        p1[multiplier]+=5
                        p1[y]-=15
                    attack2[0]=0
    if click[1]==False:    #end attack
        attack2[0]=0
            
    if attack2[1]==True and n[y]>150:  #>150 fixes a bug where the player fell through the platform
        attack3Sound.play()# sound effect
        if attack2[1]==True:
            n[y]+=n[vy]
            n[vy]+=3  #faster gravity
        if n[y]==p1[y]:   #if they both have the same y value
            if p1[x]-n[x]<=0 and p1[x]-n[x]>=-20  and attack[3]==False: #knockback left
                if p1[multiplier]<=80:
                    p1[x]-=50
                    p1[multiplier]+=20
                    p1[y]-=25
                else:
                    p1[multiplier]+=20
                    p1[x]-=50*(p1[multiplier]//80)
                    p1[y]-=25       #vertical knockback
            elif p1[x]-n[x]>0 and p1[x]-n[x]<20  and attack[3]==False:  #knockback right
                if p1[multiplier]<=80:
                    p1[x]+=50
                    p1[multiplier]+=20
                    p1[y]-=25
                else:
                    p1[multiplier]+=20
                    p1[x]+=50*(p1[multiplier]//80)
                    p1[y]-=25
        attack2[1]=False
           

    if attack2[2]==True:  #close attack
        attack3Sound.play()
        if n[x]>p1[x]-30 and n[x]<p1[x]+30:
            if n[y]+8>p1[y]-29 and n[y]+8<p1[y]+29  and attack[3]==False: #block has to equal false
                if n[direction]=="left":
                    if p1[multiplier]<80:
                        p1[multiplier]+=15
                        p1[x]-=15
                        p1[y]-=15
                    else:
                        p1[multiplier]+=15   #increase multiplier
                        p1[x]-=15*(p1[multiplier]//80)
                        p1[y]-=15
                elif n[direction]=="right":
                    if p1[multiplier]<80:
                        p1[x]+=15
                        p1[multiplier]+=15
                        p1[y]-=15   #vertical knockback
                    else:
                        p1[multiplier]+=15
                        p1[x]+=15*(p1[multiplier]//80)
                        p1[y]-=15
        attack2[2]=False    #end attack
        
    if attack2[3]==True:   #block
        if n[ground]==True:   #must be on the ground
            if stop[1]>=60:
                stop[1]=0
                attack2[3]=False
            if stop[1]<60:
                stop[1]+=1
                n[x]=bx[1]
                
def addPics1(name,start,end):  #sprites for p1
    mypics1=[]
    myNewpics1=[]  #for bowser
    for i in range(start,end+1):   #range of pics
        mypics1.append(image.load("%s/%s%03d.png" %(name,name,i)))  #appends pics
    if name=="bowser":
        for x in mypics1:
            newSize=transform.smoothscale(x,(38,38))  #shrinks bowser
            myNewpics1.append(newSize)  #appends bowser pics
        return myNewpics1
    return mypics1

def addPics2(name,start,end):   #sprites for computer or p2
    mypics2=[]   
    myNewpics2=[]   #for bowser
    for i in range(start,end+1): #start to end is the range of pics
        mypics2.append(image.load("%s/%s%03d.png" %(name,name,i))) #appends images to list
    if name=="bowser":
        for x in mypics2:   #shrinks bowser
            newSize=transform.smoothscale(x,(38,38))
            myNewpics2.append(newSize)  #appends scaled bowser
        return myNewpics2
        
    return mypics2

    
pics1=[]  #empty list for p1 sprites
pics2=[]     #empty list for p2 sprites
def sprites():
    if Character!="Unchosen":   #if a character is chosen
        pics1.append(addPics1(char[0],1,movel[0]))  #char is charcter, movel is pics facing left
        pics1.append(addPics1(char[0],movel[0]+1,mover[0])) #all pics after are facing right

        pics2.append(addPics2(char[1],1,movel[1]))  #pics facing left
        pics2.append(addPics2(char[1],movel[1]+1,mover[1]))  #pics facing right


##########################
page="menu"
myclock=time.Clock()
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False

    ##
     
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    
    if stadium==("Unchosen"):  #once a stadium is chosen the game begins and the menu stops
        mixer.music.load("music/menu.mp3")  #music
        mixer.music.play(-1)
        if page == "menu":
            page = menu()
        if page == "game":
            page = Game()    
        if page == "instructions":
            page = instructions()    
        if page == "close":
            try:
                quit()
            except pygame.error:
                pass
            page = close()
            
        if page == "credits":
            page = credit()
    else:                           #when a stadium is chosen the game starts
        if Character!="Unchosen": #decreases lag from bowser
            sprites()
        P1(player[0], player[1],attack[0])
        P2(player[1], player[0],attack[1])
        AI(player[0],computer,attack[1])
        drawScene(screen,player[0],player[1],pics1,pics2,computer,attack[0],attack[1])
        checkCollision(player[0],player[1],attack[0],attack[1],computer)
        attacks(player[0],player[1],attack[0],attack[1],computer)
        Restart(player[0])
   
    ###


    myclock.tick(60)
    
    display.flip()
quit()
