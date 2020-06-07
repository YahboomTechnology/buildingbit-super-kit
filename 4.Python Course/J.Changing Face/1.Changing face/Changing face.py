from microbit import *
import superbit
import microbit
import random

superbit.servo270(superbit.S1, 50)
microbit.sleep(500)
superbit.servo270(superbit.S1, 140)
display.scroll("Go!")

def Face_show():
    global a
    a = random.randint(1, 7)
    if a == 1:
        display.show(Image.HAPPY)
    elif a == 2:
        display.show(Image.ANGRY)
    elif a == 3:
        display.show(Image.SMILE)
    elif a == 4:
        display.show(Image.CONFUSED)
    elif a == 5:
        display.show(Image.SAD)
    elif a == 6:
        display.show(Image.HEART)

while True:
    superbit.servo270(superbit.S1, 50)
    microbit.sleep(200)
    Face_show()
    microbit.sleep(200)
    superbit.servo270(superbit.S1, 140)
    microbit.sleep(1000)