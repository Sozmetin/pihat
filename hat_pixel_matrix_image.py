from sense_hat import SenseHat
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)

pixels = [
    w,r,w,w,w,w,r,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,b,b,w,w,w,
    r,w,w,w,w,w,w,r,
    w,r,r,r,r,r,r,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    ]

sense.set_pixels(pixels)
sense.clear()
