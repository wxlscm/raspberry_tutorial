import turtle
import random
pat = turtle.Turtle()
turtle.Screen().bgcolor("grey")
#turtle.speed(5)
#turtle.Turtle().screen.delay(0)

colours = ["cyan", "purple", "white", "blue"]



pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)
    
    
for i in range(8):
    branch()
    pat.left(45)


