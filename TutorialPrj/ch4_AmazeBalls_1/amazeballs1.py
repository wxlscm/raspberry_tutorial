import pgzrun

player = {"x":0, "y":3, "frame":0, "sx":0, "sy":0,
          "moveX":0, "moveY":0, "queueX":0, "queueY":0,
          "moveDone":True, "movingNow":False, "animCounter":0}
OFFSETX = 368
OFFSETY = 200

mapData = [[1,1,1,0,1,1,1,1,1,1,1,1],
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
mapBlocks = ["map1c","map2c"]

mapHeight = [0,32]
mazeSolved = False

def draw(): # Pygame Zero draw function
    screen.fill((0, 0, 0))
    drawMap()
    screen.blit('title', (200, 0))
    if mazeSolved :
        screen.draw.text("MAZE SOLVED!" , center=(400, 300), owidth=0.5, ocolor=(0,0,0), color=(0,255,0) , fontsize=60)

def update(): # Pygame Zero update function
    global player
    if player["moveDone"] == True:
        if keyboard.left: doMove(player, -1, 0)
        if keyboard.right: doMove(player, 1, 0)
        if keyboard.up: doMove(player, 0, -1)
        if keyboard.down: doMove(player, 0, 1)
    updateBall(player)

def drawMap():
    for x in range(0, 12):
        for y in range(0, 12):
            screen.blit(mapBlocks[mapData[x][y]], ((x*32)-(y*32)+OFFSETX,
                        (y*16)+(x*16)+OFFSETY - mapHeight[mapData[x][y]]))
            if x == player["x"] and y == player["y"]:
                if player["sx"] == 0:
                   player["sx"] = (x*32)-(y*32)+OFFSETX
                   player["sy"] = (y*16)+(x*16)+OFFSETY-32
                screen.blit("ball"+str(player["frame"]), (player["sx"], player["sy"]))

def doMove(p, x, y):
    if 0 <= (p["x"]+x) < mapInfo["width"] and 0 <= (p["y"]+y) < mapInfo["height"]:
        if mapData[p["x"]+x][p["y"]+y] == 0:
            p.update({"queueX":x, "queueY":y, "moveDone":False})
              
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

def moveP(p,x,y):
    p["sx"] += x
    p["sy"] += y
    
pgzrun.go()
