#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

while True:
    rc = random.randint (0, 255)
    rc2 = random.randint (0, 255)
    rc3 = random.randint (0, 255)
    rx = random.randint (0, 7)
    ry = random.randint (0, 7)

    sense.set_pixel(rx, ry, (rc, rc2, rc3))
    time.sleep(3)
    sense.clear()
    time.sleep(1)

