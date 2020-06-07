from microbit import *
import superbit
import microbit
import neopixel

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
superbit.servo270(superbit.S1, 90)

while True:
    display.show(Image.ARROW_N)
    np[0] = (255, 0, 0)
    np[1] = (255, 0, 0)
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    np.show()
    superbit.servo270(superbit.S1, 0)
    microbit.sleep(500)
    display.show(Image.ARROW_S)
    np[0] = (0, 255, 0)
    np[1] = (0, 255, 0)
    np[2] = (0, 255, 0)
    np[3] = (0, 255, 0)
    np.show()
    superbit.servo270(superbit.S1, 90)
    microbit.sleep(1000)