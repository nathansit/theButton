import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import logging
import datetime
logger = logging.getLogger()
logger.setLevel("DEBUG")

GPIO.setmode(GPIO.BOARD)

#ledPin = 12
#buttonPin = 16
buttonPin = 12

broker="homeassistant.local"

def on_publish(client, userdata, result):
    print("data publish \n")

client = mqtt.Client("python1")
client.on_publish = on_publish
client.username_pw_set("localmqtt", "Ezekiel 10:19")

# connect to broker

#GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# def countClicks() # count the number of clicks and then use that to determine the funciton

# time between last press
DOWN = False
UP = True

prevState = UP
currState = UP

# modified to detect a change in the state of button
while True:
    time.sleep(0.1)
    currState =  GPIO.input(buttonPin)
#	print(buttonState)
    # if button state is switched
    if currState != prevState:

        # reset the prevState
        prevState = currState
        print("button changed!")
        # send a message
        client.connect(broker)
        client.publish("pi/nathan/button/1", "single_click")
        client.disconnect()
    else:
        # client.publish("pi/nathan/button/1", "single_click")
        pass

