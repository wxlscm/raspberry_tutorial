from sense_hat import SenseHat
from collections import deque
import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

windowWidth = 720
windowHeight = 400
offsetX=10
offsetY=windowHeight/2

sense = SenseHat()
sense.clear()
pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((windowWidth, windowHeight) )  #pygame.FULLSCREEN
pygame.display.set_caption('Accelerometer Demo')
textFont = pygame.font.SysFont("kalinga", 12)
xqueue=deque()
yqueue=deque()
zqueue=deque()

def draw_Coord_Sys():
    pygame.draw.line(surface, (255,255,255),(offsetX,0), (offsetX,windowHeight) , 3)
    pygame.draw.line(surface, (255,255,255),(offsetX,offsetY),
                     (windowWidth,offsetY) , 3)
    renderedText = textFont.render("(g)", 0, (255,255,255))   #1
    surface.blit(renderedText, (offsetX+9, 10))   
    #画刻度
    kedu_up=-1.5
    kedu_down=0.5
    for i in range(1,4):
        pygame.draw.line(surface, (255,255,255),(offsetX+2,50*i),
                         (offsetX+6,50*i) , 2)
        pygame.draw.line(surface, (255,255,255),(offsetX+2,50*i+offsetY),
                         (offsetX+6,50*i+offsetY) , 2)
        renderedText = textFont.render(str(kedu_up), 0, (255,255,255))   #1
        surface.blit(renderedText, (offsetX+9, 50*i-7))   
        renderedText = textFont.render(str(kedu_down), 0, (255,255,255))   #1
        surface.blit(renderedText, (offsetX+9, 50*i-7+offsetY))   
        kedu_up+=0.5
        kedu_down+=0.5


def quitGame():
    pygame.quit()
    sys.exit()

while True:
    surface.fill((0,0,0))
    draw_Coord_Sys()
    acceleration = sense.get_accelerometer_raw()
    xqueue.append(int(acceleration['x']*100) )
    yqueue.append(int(acceleration['y']*100) )
    zqueue.append(int(acceleration['z']*100) )
    if len(xqueue)>=windowWidth-offsetX:
        xqueue.popleft()
        yqueue.popleft()
        zqueue.popleft()

    for i in range(len(xqueue)-1):
        pygame.draw.line(surface, (255,0,0),
                         (offsetX+i,offsetY+xqueue[i]), 
                         (offsetX+i+1,offsetY+xqueue[i+1]),
                         1)
        pygame.draw.line(surface, (255,255,0),
                         (offsetX+i,offsetY+yqueue[i]), 
                         (offsetX+i+1,offsetY+yqueue[i+1]),
                         1)
        pygame.draw.line(surface, (0,255,0),
                         (offsetX+i,offsetY+zqueue[i]), 
                         (offsetX+i+1,offsetY+zqueue[i+1]),
                         1)
        
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()   
    pygame.display.update()







