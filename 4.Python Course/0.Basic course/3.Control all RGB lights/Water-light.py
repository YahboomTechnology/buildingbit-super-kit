from microbit import *
import neopixel

display.show(Image.HAPPY)

np = neopixel.NeoPixel(pin12, 4)
np.clear()
np.show()

while True:
    np[0] = (0, 255, 0)
    np.show()
    sleep(200)
    np[1] = (0, 255, 0)
    np.show()
    sleep(200)
    np[2] = (0, 255, 0)
    np.show()
    sleep(200)
    np[3] = (0, 255, 0)
    np.show()
    sleep(200)
    np.clear()
    np.show()
    sleep(200)