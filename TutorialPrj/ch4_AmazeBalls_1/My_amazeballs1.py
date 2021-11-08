import pygame,sys
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

windowWidth = 800
windowHeight = 700

OFFSETX = 368
OFFSETY = 250

player = {"x":0, "y":3, "frame":0, "sx":0, "sy":0,
          "moveX":0, "moveY":0, "queueX":0, "queueY":0,
          "moveDone":True, "movingNow":False, "animCounter":0}

mazeSolved = False

mapData = [[1,1,1,0,1,1,1,1,1,1,1,1],      #[1,1,1,0,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,0,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,0,0,0,1],
           [1,0,0,0,0,0,0,1,0,1,1,1],
           [1,0,1,0,1,1,0,1,0,0,0,1],
           [1,0,1,0,1,0,0,1,1,1,0,1],
           [1,0,1,0,1,0,0,0,0,0,0,1],
           [1,1,1,0,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,0,1,1,1]]
mapInfo = {"width":12, "height":12}

mapHeight = [0,32]

BallImages=[]

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((windowWidth, windowHeight) )  
pygame.display.set_caption('3D Maze game part 1')
textFont = pygame.font.SysFont("monospace", 25)
title_image = pygame.image.load("images/title.png")
map1c_image=pygame.image.load("images/map1c.png")
map2c_image=pygame.image.load("images/map2c.png")
for i in range(8):
    BallImages.append( pygame.image.load("images/ball%01d.png" % i) )
    
mapBlocks = [map1c_image, map2c_image]
    
def draw(): # Pygame Zero draw function
    surface.fill((0, 0, 0))
    drawMap()
    surface.blit(title_image, (200, 0))
    if mazeSolved :
        renderedText = textFont.render("MAZE SOLVED!", 1, (0,255,0))   #1
        surface.blit(renderedText, (400, 310))   #  495, 430
      #  surface.draw.text("MAZE SOLVED!" , center=(400, 300), owidth=0.5,
       #                  ocolor=(0,0,0), color=(0,255,0) , fontsize=60)

def drawMap():
    for x in range(0, 12):
        for y in range(0, 12):
            surface.blit(mapBlocks[mapData[x][y]], ((x*32)-(y*32)+OFFSETX,
                        (y*16)+(x*16)+OFFSETY - mapHeight[mapData[x][y]]))
            if x == player["x"] and y == player["y"]:
                if player["sx"] == 0:
                   player["sx"] = (x*32)-(y*32)+OFFSETX
                   player["sy"] = (y*16)+(x*16)+OFFSETY-32
                surface.blit(    BallImages[ player["frame"] ],
                              (player["sx"], player["sy"]))
                
def doMove(p, x, y):
    if 0 <= (p["x"]+x) < mapInfo["width"] and 0 <= (p["y"]+y) < mapInfo["height"]:
        if mapData[p["x"]+x][p["y"]+y] == 0:
            p.update({"queueX":x, "queueY":y, "moveDone":False})

def moveP(p,x,y):
    p["sx"] += x
    p["sy"] += y

def quitGame():
    pygame.quit()
    sys.exit()

def updateBall(p):
    global mazeSolved
    if p["movingNow"]:
        if p["moveX"] == -1: moveP(p,-1,-0.5)
        if p["moveX"] == 1: moveP(p,1,0.5)
        if p["moveY"] == -1: moveP(p,1,-0.5)
        if p["moveY"] == 1: moveP(p,-1,0.5)
    p["animCounter"] += 1
    if p["animCounter"] == 4:
        p["animCounter"] = 0
        p["frame"] += 1
        if p["frame"] > 7:
            p["frame"] = 0
        if p["frame"] == 4:
            if p["moveDone"] == False:
                if p["queueX"] != 0 or p["queueY"] !=0:
                    p.update({"moveX":p["queueX"], "moveY":p["queueY"],
                              "queueX":0, "queueY":0, "movingNow": True})            
            else:
                p.update({"moveX":0, "moveY":0, "movingNow":False})
                if p["x"] == 11 and p["y"] == 8: mazeSolved = True

        if p["frame"] == 7 and p["moveDone"] == False and p["movingNow"] == True:
            p["x"] += p["moveX"]
            p["y"] += p["moveY"]
            p["moveDone"] = True



while True:
    draw()
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
            elif event.key == pygame.K_LEFT:
                doMove(player, -1, 0)
            elif event.key == pygame.K_RIGHT:
                doMove(player, 1, 0)
            elif event.key == pygame.K_UP:
                doMove(player, 0, -1)
            elif event.key == pygame.K_DOWN:
                doMove(player, 0, 1)
    updateBall(player)      
    pygame.display.update()



