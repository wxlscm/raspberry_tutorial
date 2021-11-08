from tkinter import *
from sense_hat import SenseHat
import time

sense = SenseHat()

class App:
    
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Pitch Direction', font=("Helvetica", 32))
        label.grid(row=0)
        self.reading_label = Label(frame, text='12.34', font=("Helvetica", 110))
        self.reading_label.grid(row=1)
        self.update_reading()

    def update_reading(self):
        o = sense.get_orientation()
        reading_str = str( int(o['pitch'] ) )
        self.reading_label.configure(text=reading_str)
        self.master.after(500, self.update_reading)
        
root = Tk()
root.wm_title('Board orientation Demo')
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()

