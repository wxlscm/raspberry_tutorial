from bottle import route,run
from sense_hat import SenseHat
import sys
sense = SenseHat()

flag1=0
if len(sys.argv) != 2:
    print("usage:", sys.argv[0], "<host>")
    sys.exit(1)
host= sys.argv[1]

def flagup():
    print('key pressed!')
    global flag1
    flag1=1
sense.stick.direction_up = flagup

led_states = [0, 0, 0]
def joystick_status():
    global flag1
    x=flag1
    if x==1:
        flag1=0
        return 'Down'
    else:
        return 'UP'

def html_for_led(led):
    l = str(led)
    result = " <input type='button' onClick='changed(" + l + ")' value='LED "
                + l + "'/>"
    return result

def update_leds():
    sense.clear()
    for i, value in enumerate(led_states):
        if(value !=0):
            sense.set_pixel(i, 2+i, (255, 0, 0))

@route('/')  
@route('/<led>')
def index(led="n"):
    print(led)
    if led != "n":
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "  window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>Sense Hat LED</h1>'
    response += '<h2>Button=' + joystick_status() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += html_for_led(0) 
    response += html_for_led(1) 
    response += html_for_led(2) 
    return response

run(host=host, port=80)