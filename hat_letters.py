#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

#RGB values
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
white = (255, 255, 255)
gray = (155, 155, 155)
raspberry = (255, 0, 125)
black = (0, 0, 0)

sense.show_letter("A", red)
time.sleep(1)
sense.show_letter("B", blue)
time.sleep(1)
sense.show_letter("C", green)
time.sleep(1)
sense.show_letter("D", white)
time.sleep(1)
sense.show_letter("E", raspberry)
time.sleep(1)
sense.clear()

