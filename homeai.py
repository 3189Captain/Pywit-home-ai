import sys
from wit import Wit
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
access_token = 'DUZHEUWPEYMKAKAHRM3GSVE2RO6QT5UT'

w = [150, 150, 150]
r = [255, 0, 0]
e = [0, 0, 0]

light = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
]
smile = [
e,e,e,e,e,e,e,e,
e,r,r,e,e,r,r,e,
e,r,r,e,e,r,r,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,r,e,
e,r,r,e,e,r,r,e,
e,e,e,r,r,e,e,e,
e,e,e,e,e,e,e,e,
]

def send(request, response):
    print(response['text'])

def turn_on_lights(request):
    context = request['context']
    print "lights on"
    sense.set_pixels(light)
    return context
    
def turn_off_lights(request):
    context = request['context']
    print "lights off"
    sense.clear()
    return context

def show_smile(request):
    context = request['context']
    sense.set_pixels(smile)
    sleep(3)
    sense.clear()
    return context

def show_name(request):
    context = request['context']
    sense.show_message("Alfred, the home assistance AI", scroll_speed = 0.05)
    return context

def exit_alfred(request):
    sense.clear()
    exit(1)


actions = {
    'send' : send,
    'turn_on_lights' : turn_on_lights,
    'turn_off_lights' : turn_off_lights,
    'exit_alfred' : exit_alfred,
    'show_smile' : show_smile,
    'show_name' : show_name,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
