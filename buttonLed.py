import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import logging
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
while True:
	buttonState = GPIO.input(buttonPin)
#	print(buttonState)
	if buttonState == False:
#		GPIO.output(ledPin, GPIO.HIGH)
		# send a message
		client.connect(broker)
		client.publish("pi/nathan/button/1", "single_click")
		time.sleep(0.2)
		client.disconnect()
		pass
	else:
		# client.publish("pi/nathan/button/1", "single_click")
		time.sleep(0.05)

		pass

