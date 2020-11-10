# -*- coding: utf-8 -*-
# Python 3.7 is recommanded

# import Raspberry GPIO module
import RPi.GPIO as GPIO
# import time module
import time
import random

# set rgb pin
redPin   = 22
greenPin = 18
bluePin  = 16

print('running...')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def offAll():
    GPIO.output(bluePin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(redPin, GPIO.LOW)

def foo():
    i=0
    times = random.randint(1,3)
    while i < int(times):
        color = random.choice('rgb')
        if color == 'r':
            GPIO.output(redPin, GPIO.HIGH)
        elif color == 'g':
            GPIO.output(greenPin, GPIO.HIGH)
        elif color == 'b':
            GPIO.output(bluePin, GPIO.HIGH)
        i = i + 1
    time.sleep(0.2)
    offAll()



while True:
    foo()
