#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

#RGB values
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

speed = 0.05

message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sense.show_message(message, speed, text_colour=black, back_colour=white)

sense.clear()
