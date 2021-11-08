import os, time, datetime
from sense_hat import SenseHat

def log_temp():
    o = sense.get_orientation()
    reading_str = str( int(o['pitch'] ) )
    
    dt = datetime.datetime.now()
    with open(filename,'a') as f:
        f.write('"{:%H:%M:%S}",'.format(dt))
        f.write(reading_str+"\n")
    print('"{:%H:%M:%S}",'.format(dt)+reading_str)
    f.close()

running = True
log_period = 5 # seconds
dt = datetime.datetime.now()
sense = SenseHat()
filename = 'write_data.txt'
print("Logging to: " + filename)

while running:
    try:
        log_temp()
        time.sleep(log_period)
    except KeyboardInterrupt:
        print ('Program stopped')
        running = False
     #   file.close()