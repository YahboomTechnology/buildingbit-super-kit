from microbit import *
import superbit
import microbit
import neopixel

np = neopixel.NeoPixel(pin12, 4)
fan = Image("00990:90900:99999:00909:09900")
display.show(fan)

global a, b, angle
angle = 135
b = 0
superbit.servo270(superbit.S1, angle)
microbit.sleep(1000)

while True:
    superbit.motor_control(superbit.M1, 225, 0)
    if b == 0:
        superbit.servo270(superbit.S1, angle)
        angle = angle + 1
        if angle > 270:
            angle = 270
            b = 1
    elif b == 1:
        superbit.servo270(superbit.S1, angle)
        angle = angle - 1
        if angle < 0:
            angle = 0
            b = 0