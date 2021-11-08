from tkinter import *
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

redValue=0
greenValue=0
blueValue=0

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Red').grid(row=0, column=0)
        Label(frame, text='Green').grid(row=1, column=0)
        Label(frame, text='Blue').grid(row=2, column=0)
        scaleRed = Scale(frame, from_=0, to=255,
              orient=HORIZONTAL, command=self.updateRed)
        scaleRed.grid(row=0, column=1)
        scaleGreen = Scale(frame, from_=0, to=255,
              orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.grid(row=1, column=1)
        scaleBlue = Scale(frame, from_=0, to=255,
              orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.grid(row=2, column=1)


    def updateRed(self, duty):
        global redValue
        global greenValue
        global blueValue
        redValue=duty
        sense.clear(int(redValue), int(greenValue), int(blueValue) )

    def updateGreen(self, duty):
        global redValue
        global greenValue
        global blueValue
        greenValue=duty
        sense.clear(int(redValue), int(greenValue), int(blueValue) )
    
    def updateBlue(self, duty):
        global redValue
        global greenValue
        global blueValue
        blueValue=duty
        sense.clear(int(redValue), int(greenValue), int(blueValue) )

root = Tk()
root.wm_title('Sense Hat RGB Control')
app = App(root)
root.geometry("200x150+0+0")
root.mainloop()