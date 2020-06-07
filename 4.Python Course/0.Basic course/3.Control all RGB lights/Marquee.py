from microbit import *
import neopixel

display.show(Image.HAPPY)

np = neopixel.NeoPixel(pin12, 4)
np.clear()
np.show()

while True:
    np[0] = (0, 255, 0)
    np[1] = (255, 255, 0)
    np[2] = (0, 255, 255)
    np[3] = (255, 255, 255)
    np.show()
    sleep(200)
    np[0] = (255, 255, 0)
    np[1] = (255, 0, 0)
    np[2] = (0, 0, 255)
    np[3] = (255, 0, 255)
    np.show()
    sleep(200)
    np[0] = (0, 0, 255)
    np[1] = (255, 130, 28)
    np[2] = (125, 90, 255)
    np[3] = (255, 0, 0)
    np.show()
    sleep(200)
    np[0] = (0, 255, 0)
    np[1] = (255, 255, 0)
    np[2] = (90, 190, 200)
    np[3] = (255, 0, 180)
    np.show()
    sleep(200)
