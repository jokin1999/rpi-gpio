# -*- coding: utf-8 -*-
# Python 3.7 is recommanded
# This file is for HC-SR04

# import Raspberry GPIO module
import RPi.GPIO as GPIO
# import time module
import time

# set trig pin
trig = 11
# set echo pin
echo = 13

print('running...')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def run():
    # send a start signal
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(trig, GPIO.LOW)

    # filter useless signal
    while GPIO.input(echo) == GPIO.LOW:
        continue

    # input flag
    first = 0
    # time span count
    count = 0

    # read signal lasting time
    while GPIO.input(echo) == GPIO.HIGH:
        if first == 0:
            first = 1
        # 10us
        time.sleep(0.00001)
        count += 1

    # calculate distance (m)
    dis = count * 10 * 3.4 * 0.001 / 2
    # calculate distance (cm)
    dis = dis * 100

    # print distance
    print(str(dis) + "cm")

# keep running
while True:
    run()
    time.sleep(0.5)
    continue
