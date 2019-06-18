from sense_hat import SenseHat
sense = SenseHat()
import time
import random

while True:
    l = random.randint(0,7)
    w = random.randint(0,7)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    sense.set_pixel(l,w,(r,g,b))
    sense.set_pixel(l,w,(0,0,0))
    time.sleep(1)
    sense.clear()
    time.sleep(1)
