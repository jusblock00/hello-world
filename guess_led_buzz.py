#!/usr/bin/env python
import random
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,3000)

def buzz(freq, seconds):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(seconds)
    Buzz.stop()

#UNUSED CODE FROM PRESENTATION SLIDE
#def display_message(status):
    #if status == 'right':
       #print 'you guessed it'
    #else:
        #print 'guess too', status

#generate a random number from 1 to 10
n = random.randint(1,10)
t = 1
#keep running until number is guessed
while True:
    print ('\nGuess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print 'Your guess is too low'
        t = t + 1
        buzz(100, .5)
        GPIO.cleanup()
    elif guess > n:
        print 'Your guess is too high'
        t = t + 1
        buzz(1000, .5)
        GPIO.cleanup()
    else:
        print '\nYou guessed the number', n
        if t > 1:
            print 'It took you', t, 'tries'
        else:
            print 'It took you only one try. Lucky guess!'
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        led_pin = 11
        GPIO.setup(led_pin,GPIO.OUT)
        GPIO.output(led_pin,True)
        buzz(200, .5)
        buzz(300, .75)
        buzz(400, 1)
        GPIO.output(led_pin,False)
        GPIO.cleanup()
        
        #LED CODE ONLY
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        #led_pin = 11
        #GPIO.setup(led_pin,GPIO.OUT)
        #GPIO.output(led_pin,True)
        #time.sleep(5)
        #GPIO.output(led_pin,False)
        #GPIO.cleanup()
        break
