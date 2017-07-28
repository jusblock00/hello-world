#!/usr/bin/env python
#script uses the Touch Switch to toggle on/off sensors
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
led_pin = 11

GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(led_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,500)

def buzz(freq, seconds, stop):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(seconds)
    Buzz.stop()
    time.sleep(stop)

frequences = [300, 300, 450, 450, 500, 500, 450, 390, 390, 350, 350, 330, 330, 300, 450, 450, 390, 390, 350, 350, 330, 450, 450, 390, 390, 350, 350, 330]
times = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
stop = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.1 , 0.1, 0.1, 0.1, 0.1]

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Touch Switch; pin 31 = GPIO 6
touch_pin = 31

#set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)

#create infinite loop that toggles on and off when touched
while True:
    if GPIO.input(touch_pin) == 0:
        for i in range(len(frequences)):
            buzz(frequences[i], times[i], stop[i])
        GPIO.output(led_pin, True)
        #code to toggle off
    if GPIO.input(touch_pin) == 1:
        Buzz.stop()
        GPIO.output(led_pin, False)
        #code to toggle on

GPIO.cleanup()

    
