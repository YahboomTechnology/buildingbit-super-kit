from microbit import *
import superbit
import music

superbit.servo270(superbit.S1, 90)
while True:
    display.show(Image.HEART)
    if button_a.is_pressed() is True and button_b.is_pressed() is False:
        display.show(Image.ARROW_W)
        music.play('B6:8')
        superbit.servo270(superbit.S1, 0)
    elif button_a.is_pressed() is False and button_b.is_pressed() is True:
        display.show(Image.ARROW_E)
        music.play('C3:4')
        superbit.servo270(superbit.S1, 90)