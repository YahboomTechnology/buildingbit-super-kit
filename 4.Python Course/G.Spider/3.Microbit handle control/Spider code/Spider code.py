from microbit import *
import superbit
import radio
import neopixel

radio.on()
radio.config(group=1)
display.show(Image("09090:09090:00900:09090:09090"))
np = neopixel.NeoPixel(pin12, 4)

while True:
    incoming = radio.receive()
    if incoming == 'up':
        superbit.motor_control(superbit.M1, -255, 0)
        superbit.motor_control(superbit.M3, -255, 0)
    elif incoming == 'down':
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, 255, 0)
    elif incoming == 'left':
        superbit.motor_control(superbit.M1, 255, 0)
        superbit.motor_control(superbit.M3, -255, 0)
    elif incoming == 'right':
        superbit.motor_control(superbit.M1, -255, 0)
        superbit.motor_control(superbit.M3, 255, 0)
    elif incoming == 'stop':
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)

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
        np[0] = (255, 255, 255)
        np[1] = (255, 255, 255)
        np[2] = (255, 255, 255)
        np[3] = (255, 255, 255)
        np.show()

    elif incoming == 'turn_off':
        np.clear()
        np.show()