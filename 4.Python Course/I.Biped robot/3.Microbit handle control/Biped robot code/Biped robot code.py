from microbit import *
import superbit
import radio
import neopixel
import microbit

np = neopixel.NeoPixel(pin12, 4)

display.show(Image.HEART)
microbit.sleep(1000)
radio.on()
radio.config(group=1)
mode = 1

while True:
    display.show(mode)
    incoming = radio.receive()
    if incoming == 'up':
        superbit.motor_control(superbit.M1, -255, 0)
    elif incoming == 'down':
        superbit.motor_control(superbit.M1, 255, 0)
    elif incoming == 'stop' and mode == 1:
        superbit.motor_control(superbit.M1, 0, 0)
    elif incoming == 'turn_off':
        np.clear()
        np.show()
        if mode == 1:
            mode = 2
        else:
            mode = 1
    if incoming == 'R':
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np.show()
        superbit.motor_control(superbit.M1, 0, 0)
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