from sense_hat import SenseHat
from time import sleep

upPushed=0
sense = SenseHat()
sense.clear()


def processUp(event):
    global upPushed
    if event.direction=="up" and event.action=="pressed" :
        print("UP press event!")
        upPushed=1
#    elif event.direction=="up" and event.action=="held" :
#        print("UP held event!")



sense.stick.direction_up = processUp

while True:
    if upPushed==0:
        sense.set_pixel(0, 2, (255, 0, 0))     #red
        sleep(5)
        sense.set_pixel(0, 4, (255, 255, 0))     #yellow
        sleep(2)
        sense.set_pixel(0, 2, (0, 0, 0))     #set blank
        sense.set_pixel(0, 4, (0, 0, 0))     #set blank
        sense.set_pixel(0, 6, (0, 255, 0))     #green
        sleep(5)
        sense.set_pixel(0, 6, (0, 0, 0))     #green
    else:
        sense.set_pixel(0, 2, (255, 0, 0))     #red
        for i in range(10):
            sense.set_pixel(0, 7, (255, 255, 255))     #white
            sleep(0.2)
            sense.set_pixel(0, 7, (0, 0, 0)) 
            sleep(0.2)
        sense.set_pixel(0, 2, (0, 0, 0))     #red
        sleep(1)     #add
        upPushed=0
        
        
        
        
    

