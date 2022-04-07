##############################################################################
## Name: Broady Rivet
## Date: 10/17/18
## Description: LED blinks on and off every 0.5 sec when switch is not pressed
##              and 0.1 sec when the button is pressed.
##############################################################################

##import libraries needed##
import RPi.GPIO as GPIO
from time import sleep

##set ports##
led = 17
button = 22

##make setup statements##
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

##main program##
while (True):
    if(GPIO.input(button) == GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH) 
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)
    else:
        GPIO.output(led, GPIO.HIGH) 
        sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        sleep(0.5)
