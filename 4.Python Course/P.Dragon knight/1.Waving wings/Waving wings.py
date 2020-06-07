from microbit import *
import superbit
import microbit

display.show(Image.HAPPY)

while True:
    superbit.motor_control(superbit.M1, 255, 0)
