import sys
from wit import Wit


access_token = 'DUZHEUWPEYMKAKAHRM3GSVE2RO6QT5UT'



def send(request, response):
    print(response['text'])

def turn_on_lights(request):
    context = request['context']
    print "lights on"
    return context
    
def turn_off_lights(request):
    context = request['context']
    print "lights off"
    return context

def exit_alfred(request):
    exit(1)


actions = {
    'send' : send,
    'turn_on_lights' : turn_on_lights,
    'turn_off_lights' : turn_off_lights,
    'exit_alfred' : exit_alfred,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
