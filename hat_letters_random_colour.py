#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

n = 0

#sense.show_message("And a...")

yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

speed = 0.05

message = "And a..."

sense.show_message(message, speed, text_colour=red, back_colour=black)

while n < 3:
    r = random.randint (0, 255)
    r2 = random.randint (0, 255)
    r3 = random.randint (0, 255)
    n = n + 1
    sense.show_letter("1", (r2, 0, r))
    time.sleep(0.5)
    sense.show_letter("2", (0, r, r3))
    time.sleep(0.5)
    sense.show_letter("3", (r3, r2, 0))
    time.sleep(0.5)
    sense.show_letter("4", (r, r2, r3))
    time.sleep(0.5)
sense.clear()

