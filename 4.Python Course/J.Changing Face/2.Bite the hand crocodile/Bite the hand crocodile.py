from microbit import *
import superbit
import microbit
import random

superbit.servo270(superbit.S1, 50)
microbit.sleep(500)
superbit.servo270(superbit.S1, 140)
display.scroll("Go!")
display.show(Image.ANGRY)


global a
global button_down
button_down = 0
while True:

    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        if button_down == 0:
            a = random.randint(1, 3)
            if a < 3:
                superbit.servo270(superbit.S1, 140)
                a = 0
            else:
                superbit.servo270(superbit.S1, 50)
                microbit.sleep(500)
                superbit.servo270(superbit.S1, 140)
                a = 0
        button_down = 1
    if button_b.is_pressed() is True and button_a.is_pressed() is False:
        if button_down == 0:
            a = random.randint(1, 3)
            if a < 3:
                superbit.servo270(superbit.S1, 140)
                a = 0
            else:
                superbit.servo270(superbit.S1, 50)
                microbit.sleep(500)
                superbit.servo270(superbit.S1, 140)
                a = 0
        button_down = 1
    elif button_a.is_pressed() is False and button_b.is_pressed() is False:
        button_down = 0

