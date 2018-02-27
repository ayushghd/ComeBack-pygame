import pygame
import time
import random

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#FOR BACKGROUND MUSIC
pygame.mixer.music.load('gameBackground.mp3')
pygame.mixer.music.play(-1)

#DIFFERENT COLORS
white=(255,255,255)
blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)

displayWidth=900
displayHeight=600
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('ComeBack')
blockSize=30
clock=pygame.time.Clock()
FPS=30

#FONT SIZES
smallfont=pygame.font.SysFont("comicsansms",20)
mediumfont=pygame.font.SysFont("comicsansms",40)
largefont=pygame.font.SysFont("comicsansms",60)
highest=0
FPS=25

#ELEMENTS OF GAME
pill = pygame.image.load('pill.png')
bomb = pygame.image.load('bomb.png')
up = pygame.image.load('up.png')

#GAME INTRO
def introToGame():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    intro = False

        gameDisplay.fill(white)
        messageToScreen("Welcome to ComeBack!",green,-150,"large")
        messageToScreen("This game will test your memorizing power",blue,-75,"medium")
        messageToScreen("Instructions for the game are :- ",blue,-25,"medium")
        messageToScreen("Rules are simple, you have your starting point, you have to end the game at the same point",black,50,"small")
        messageToScreen("Sounds simple, isn't it? Well it's not",black,80,"small")
        messageToScreen("Think mathematically, grid size = 900x600, block size = 30x30, so total blocks = 600 ",black,110,"small")
        messageToScreen("And I forgot to tell you, As the game proceeds, speed of the object also increases",black,140,"small")
        messageToScreen("Controls -> C - Play, Q - Quit, P - Pause, Arrows - Moving, E - Mark end",blue,170,"small")
        messageToScreen("Avoid falling BOMBS, take  - PILLS to slowdown speed, UP to boost score by 200",blue,200,"small")
        messageToScreen("***ALL THE BEST***",red,230,"small")
        
        pygame.display.update()
        clock.tick(15)

def text_objects(msg,color,size):
    if size=="small":
        textSurf=smallfont.render(msg,True,color)
    elif size=="medium":
        textSurf=mediumfont.render(msg,True,color)
    elif size=="large":
        textSurf=largefont.render(msg,True,color)
    return textSurf,textSurf.get_rect()

def messageToScreen(msg,color,y_displace=0,size="small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (displayWidth/2),(displayHeight/2) + y_displace
    gameDisplay.blit(textSurf,textRect)

def pause():
    paused=True
    messageToScreen("Paused",black,-100,"large")
    messageToScreen("Press C to continue playing, Press Q to quit",black,0,"small")
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused=False        
        clock.tick(10)

def start():
    spaused=True
    messageToScreen("This is your starting point",red,-100,"medium")
    messageToScreen("Press C to continue playing, Press Q to quit",black,0,"small")
    pygame.display.update()

    while spaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    spaused=False        
        clock.tick(10)

def highscore():
    text=smallfont.render("High Score : "+str(highest),True,black)
    gameDisplay.blit(text,[730,0])
    
def score(score):
    text =  smallfont.render("Score : "+str(score),True,black)
    gameDisplay.blit(text,[0,0])

def congrats(a,b,sc):
    global highest
    paused=True
    sc=sc+1000
    messageToScreen("Congrats !",green,-150,size="large")
    messageToScreen("You successfully CameBack to your start point ("+str(a)+","+str(b)+")",black,-100,size="small")
    messageToScreen("Final Score = "+str(sc),black,-50,size="small")
    messageToScreen("Press C to continue playing, Press Q to quit",black,0,"small")
    pygame.display.update()
    if highest < sc:
        highest = sc
        
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused=False        
        clock.tick(10)

    
def sorry(a,b,c,d,sc):
    global highest
    pygame.draw.rect(gameDisplay,green,[a,b,blockSize,blockSize])
    messageToScreen("Unfortunately :(",red,-150,size="large")
    messageToScreen("You did not ComeBack to your start point",black,-100,size="small")
    k=abs(a-c)+abs(b-d)
    sc=sc-float(k)
    messageToScreen("Start Point = ("+str(a)+","+str(b)+"), End Point = ("+str(c)+","+str(d)+")",black,-70,size="small")
    messageToScreen("Final Score = Score - Diff b/w points = "+str(sc),black,-40,size="small")
    messageToScreen("Press C to continue playing, Press Q to quit",black,0,"small")
    pygame.display.update()
    paused=True
    if sc > highest :
        highest = sc
        
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused=False        
        clock.tick(10)
        
def bump():
    messageToScreen("Oh Crap!",red,-160,size="large")
    messageToScreen("You bumped into the obstacle",black,-100,size="small")
    messageToScreen("Final Score = 0",black,-70,size="small")
    messageToScreen("Press C to continue playing, Press Q to quit",black,0,"small")
    pygame.display.update()
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused=False        
        clock.tick(10)

def gameLoop():
    global highest
    gameFalse=False
    gameOver=False
    leadX=displayWidth/2
    leadY=displayHeight/2
    leadXChange=0
    leadYChange=0
    pillX=0
    pillY=0
    sc=0
    flag=0
    flag2=0
    flag3=0
    flag4=0
    bombX=0
    bombY=0
    upX=0
    upY=0
    global FPS
    
    while not gameFalse:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameFalse=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and leadXChange!=blockSize:
                    leadXChange=-blockSize
                    leadYChange=0
                elif event.key==pygame.K_RIGHT and leadXChange!=-blockSize:
                    leadXChange=blockSize
                    leadYChange=0
                elif event.key==pygame.K_UP and leadYChange!=blockSize:
                    leadYChange=-blockSize
                    leadXChange=0
                elif event.key==pygame.K_DOWN and leadYChange!=-blockSize:
                    leadYChange=blockSize
                    leadXChange=0
                elif event.key==pygame.K_p:
                    pause()
                elif event.key==pygame.K_e:
                    if startX==leadX and startY==leadY:
                        congrats(startX,startY,sc)
                    else:
                        sorry(startX,startY,leadX,leadY,sc)
                    gameLoop()

        if flag2==0 and sc%200==0 and sc>0:
            pillY=0
            pillX=round(random.randrange(0,displayWidth-blockSize)/30.0)*30.0
            flag2=1

        if flag3==0 and sc%150==0 and sc>0:
            bombY=0
            bombX=round(random.randrange(0,displayWidth-blockSize)/30.0)*30.0
            flag3=1

        if flag4==0 and sc%120==0 and sc>0:
            upY=0
            upX=round(random.randrange(0,displayWidth-blockSize)/30.0)*30.0
            flag4=1

        
        if flag==0 :
            startX=round(random.randrange(0,displayWidth-blockSize)/30.0)*30.0
            startY=round(random.randrange(0,displayHeight-blockSize)/30.0)*30.0
            leadX=startX
            leadY=startY
            
        if leadX >= displayWidth or leadX < 0 or leadY >= displayHeight or leadY < 0:
            bump()
            gameLoop()

        leadX+=leadXChange
        leadY+=leadYChange

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,blue,[leadX,leadY,blockSize,blockSize])
        
        if sc%300==0 and sc>0:
            FPS+=5
            
        if flag2==1:
            gameDisplay.blit(pill,(pillX,pillY))
            pillY+=(400/FPS)
            
            if leadX>=pillX and leadX<=pillX+blockSize or leadX + blockSize > pillX and leadX + blockSize < pillX + blockSize:
                if leadY>=pillY and leadY<=pillY+blockSize or leadY + blockSize > pillY and leadY + blockSize < pillY + blockSize:
                    FPS-=5
                    pillY+=1000
                    flag2=0

            if pillY >= displayHeight:
                flag2=0
            
        if flag3==1:
            gameDisplay.blit(bomb,(bombX,bombY))
            
            if leadX>=bombX and leadX<=bombX+blockSize or leadX + blockSize > bombX and leadX + blockSize < bombX + blockSize:
                if leadY >= bombY and leadY <= bombY+blockSize or leadY + blockSize > bombY and leadY + blockSize < bombY + blockSize:
                    bump()
                    gameLoop()

            bombY+=(400/FPS)
            if bombY >= displayHeight:
                flag3=0
            
        if flag4==1:
            gameDisplay.blit(up,(upX,upY))
            
            if leadX>=upX and leadX<=upX+blockSize or leadX + blockSize > upX and leadX + blockSize < upX + blockSize:
                if leadY >= upY and leadY <= upY+blockSize or leadY + blockSize > upY and leadY + blockSize < upY + blockSize:
                    sc+=200
                    upY+=1000
                    flag4=0

            upY+=(400/FPS)
            if upY >= displayHeight:
                flag4=0
            
            
        if leadXChange!=0 or leadYChange!=0:
            sc+=1

        score(sc)
        highscore()
        
        if flag==0:
            start()
            flag=1
        pygame.display.update()

        clock.tick(FPS)

    quit()
    pygame.quit()
        
introToGame()
gameLoop()
