import pygame
import time
import random

pygame.init()
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
smallfont=pygame.font.SysFont("comicsansms",20)
mediumfont=pygame.font.SysFont("comicsansms",40)
largefont=pygame.font.SysFont("comicsansms",60)
highest=0
FPS=30

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
        messageToScreen("Rules are simple, you choose your starting point & you have to end the game at the same point",black,50,"small")
        messageToScreen("Sounds simple, isn't it? Well it's not",black,80,"small")
        messageToScreen("Think mathematically, grid size = 900x600, block size = 30x30, so total blocks = 600 ",black,110,"small")
        messageToScreen("And I forgot to tell you, As the game proceeds, speed of the object also increases",black,140,"small")
        messageToScreen("Controls - Press C to play, Q to quit, P to pause",black,170,"small")
        messageToScreen("Arrows for moving, S to mark starting point, E to mark ending point",black,200,"small")
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
    messageToScreen("Starting Point Saved",black,-100,"medium")
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
    gameDisplay.blit(text,[750,0])
    
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
    messageToScreen("Oh crap, you bumped into the wall",red,-100,size="medium")
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
    sc=0
    flag=0
    
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
                elif event.key==pygame.K_s:
                    startX=leadX
                    startY=leadY
                    flag=1
                    start()
                elif event.key==pygame.K_e:
                    if startX==leadX and startY==leadY:
                        congrats(startX,startY,sc)
                    else:
                        sorry(startX,startY,leadX,leadY,sc)
                    gameLoop()
        
        if leadX >= displayWidth or leadX < 0 or leadY >= displayHeight or leadY < 0:
            bump()
            gameLoop()
            
        leadX+=leadXChange
        leadY+=leadYChange

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,blue,[leadX,leadY,blockSize,blockSize])
        if flag==1:
            sc+=1
        score(sc)
        highscore()
        pygame.display.update()

        clock.tick(FPS)

    quit()
    pygame.quit()
        
introToGame()
gameLoop()
