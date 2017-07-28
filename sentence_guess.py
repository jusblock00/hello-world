#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

speed = 0.015

while True:
    time.sleep(2)
    sentence = "The quick brown fox jumped over the lazy dog"
    sense.show_message(sentence, speed, text_colour=green, back_colour=black)
    sense.clear()

    print ('Type out the sentence')
    answer = raw_input()
    if answer == sentence:
        print "\nYou win!\nThe scroll speed was", speed
        break
    else:
        print "\nTry again\n"
        speed = speed + 0.005

