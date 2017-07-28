#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,3000)

def buzz(freq, seconds, stop):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(seconds)
    Buzz.stop()
    time.sleep(stop)

frequences = [300, 300, 450, 450, 500, 500, 450, 390, 390, 350, 350, 330, 330, 300]
times = [.5, .5, .5, .5, .5, .5, 1, .5, .5, .5, .5, .5, .5, 1]
stop = [.1, .1, .1, .1, .1, .1, .5, .1, .1, .1 , .1, .1, .1, .1]

for i in range(len(frequences)):
    buzz(frequences[i], times[i], stop[i])

#buzz(500, 1, 1)
#buzz(300, .5, 2)
#buzz(400, 1, 2)
#buzz(200, 2, 0)




GPIO.cleanup()
    
