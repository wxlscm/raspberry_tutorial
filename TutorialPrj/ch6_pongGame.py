from random import randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

#set bat position, random ball position, and velocity
y = 4
ball_position = [int(randint(2,6)), int(randint(1,6))]
ball_velocity = [1, 1]

#red color
X = [255, 0, 0]
#no color
N = [0, 0, 0]

#sad face array
sad_face = [
N, N, X, X, X, X, N, N,
N, X, N, N, N, N, X, N,
X, N, X, N, N, X, N, X,
X, N, N, X, N, N, N, X,
X, N, N, X, N, N, N, X,
X, N, X, N, N, X, N, X,
N, X, N, N, N, N, X, N,
N, N, X, X, X, X, N, N
]

#draws bat at y position
def draw_bat():
    sense.set_pixel(0, y, 0, 255, 0)
    sense.set_pixel(0, y+1, 0, 255, 0)
    sense.set_pixel(0, y+2, 0, 255, 0)     
    sense.set_pixel(0, y-1, 0, 255, 0)

#move bat up
def move_up(event):
    global y
    if y > 1 and (event.action=='pressed' or event.action=='held'):
        y -= 1

#move bat down
def move_down(event):
    global y
    if y < 5 and (event.action=='pressed' or event.action=='held'):  
        y += 1

#when joystick moves up or down, trigger corresponding function
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

#move ball to the next position
def draw_ball():
    #ball displayed on current position
    sense.set_pixel(ball_position[0], ball_position[1], 75, 0, 255)
    #next ball position
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    #if ball hits ceiling, calculate next position
    if ball_position[0] == 7:   
        ball_velocity[0] = -ball_velocity[0]
    #if ball hits wall, calculate next position
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    #if ball reaches 0 position, player loses and quits game
    if ball_position[0] == 0:
        sleep(0.25)
        sense.set_pixels(sad_face)
        quit()
    #if ball hits bat, calculate next ball position
    if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y+2:
        ball_velocity[0] = -ball_velocity[0]

#run the game
while True:
    sense.clear()
    draw_bat()
    draw_ball()
    sleep(0.25)
