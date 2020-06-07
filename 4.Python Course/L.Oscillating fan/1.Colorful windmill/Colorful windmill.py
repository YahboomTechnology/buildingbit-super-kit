from microbit import *
import superbit
import microbit
import neopixel

display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
superbit.servo270(superbit.S1, 135)

while True:
    superbit.motor_control(superbit.M1, 50, 0)
    np[0] = (255, 0, 0)
    np[1] = (0, 255, 0)
    np[2] = (0, 0, 255)
    np[3] = (255, 255, 255)
    np.show()
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 100, 0)
    np[0] = (255, 255, 0)
    np[1] = (0, 255, 255)
    np[2] = (0, 0, 255)
    np[3] = (255, 0, 0)
    np.show()
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 150, 0)
    np[0] = (0, 0, 255)
    np[1] = (255, 255, 255)
    np[2] = (255, 0, 255)
    np[3] = (0, 255, 0)
    np.show()
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 200, 0)
    np[0] = (125, 0, 255)
    np[1] = (70, 255, 150)
    np[2] = (0, 195, 140)
    np[3] = (255, 255, 0)
    np.show()
    microbit.sleep(1000)
    superbit.motor_control(superbit.M1, 255, 0)
    np[0] = (255, 255, 255)
    np[1] = (255, 0, 150)
    np[2] = (0, 0, 255)
    np[3] = (255, 0, 0)
    np.show()
    microbit.sleep(2000)







