from tkinter import *
from tkinter import ttk
import time
from sense_hat import SenseHat

#create an object called sense
sense = SenseHat()

#create window
window = Tk()
window.title('Local Weather Station')
window.geometry('200x480')

#create humidity label for title and value
humidity_label = Label(window, text = 'Humidity', font = ('Helvetica', 18), pady = 3)
humidity_label.pack()

humidity = StringVar()
humidity_value=Label(window, textvariable = humidity,
    font = ('Courier', 20), fg = 'blue', anchor = N, width = 200)
humidity_value.pack()

#create humidity canvas
humidity_canvas = Canvas(window, width = 200, height = 200)
humidity_canvas.pack()

#create humidity progress bar
humidity_bar = DoubleVar()
progressbar_humidity = ttk.Progressbar(humidity_canvas, variable = humidity_bar,
    orient = VERTICAL, length = 150, maximum = 100)
progressbar_humidity.pack(fill=X, expand=1)

#create temperature label for title and value
temperature_label = Label(window, text = 'Temperature', font = ('Helvetica', 18),
    anchor = S, width = 200, height = 2)
temperature_label.pack()

temperature=StringVar()
temperature_value = Label(window, textvariable = temperature, font = ('Courier', 20),
    fg = 'red', anchor = N, width = 200)
temperature_value.pack()

#create pressure label for title and value
pressure_label = Label(window, text = 'Pressure', font = ('Helvetica', 18),
    anchor = S, width = 200, height = 2)
pressure_label.pack()

pressure = StringVar()
pressure_value = Label(window, textvariable = pressure,
    font = ('Courier', 20), fg = 'green', anchor = N, width = 200)
pressure_value.pack()

def update_readings():
    humidity.set(str(round(sense.humidity, 2)) + '%')
    humidity_bar.set(sense.humidity)
    temperature.set(str(round(sense.temperature, 2)) + 'ºC')
    #temperature.set(str(round(sense.temperature*(9/5)+32, 2)) + 'ºF')
    pressure.set(str(round(sense.pressure)) + 'hPa')
    window.update_idletasks()
    window.after(3000, update_readings)

update_readings()
window.mainloop()
