from microbit import *
import superbit
import radio
import neopixel

radio.on()
radio.config(group=1)

display.show(Image.HEART)
np = neopixel.NeoPixel(pin12, 4)
superbit.servo270(superbit.S1, 50)

while True:
    incoming = radio.receive()
    if incoming == 'up':
        superbit.servo270(superbit.S1, 140)
    elif incoming == 'down':
        superbit.servo270(superbit.S1, 50)
    elif incoming == 'left':
        display.show(Image.DUCK)
    elif incoming == 'right':
        display.show(Image.COW)

    if incoming == 'R':
        np.clear()
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np.show()

    elif incoming == 'G':
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np.show()

    elif incoming == 'B':
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np[2] = (0, 0, 255)
        np[3] = (0, 0, 255)
        np.show()

    elif incoming == 'Y':
        np.clear()
        np[0] = (255, 255, 0)
        np[1] = (255, 255, 0)
        np[2] = (255, 255, 0)
        np[3] = (255, 255, 0)
        np.show()

    elif incoming == 'turn_off':
        np.clear()
        np.show()