from microbit import *
import superbit

display.show(Image.HAPPY)

while True:
    superbit.motor_control(superbit.M1, 255, 0)