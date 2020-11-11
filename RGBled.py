# -*- coding: utf-8 -*-
# Python 3.7 is recommanded

# import Raspberry GPIO module
import RPi.GPIO as GPIO
# import time module
import time
import random

# set rgb pin
redPin = 22
greenPin = 18
bluePin = 16

print('running...')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

# Turn off all colors
def offAll():
    GPIO.output(bluePin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(redPin, GPIO.LOW)


def foo():
    i = 0
    color_num = random.randint(1, 2)  # Number of colors to light
    while i < int(color_num):
        color = random.choice(['redPin', 'greenPin', 'bluePin'])
        GPIO.output(globals()[color], GPIO.HIGH)  # Select a color to light
        i = i + 1
    time.sleep(0.2)
    offAll()


while True:
    foo()
