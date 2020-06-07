# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image, sleep
import ghandle
import radio

display.show(Image.HEART)
radio.on()
radio.config(group=1)
sleep(1000)

global rocker_key
rocker_key = 0

while True:
    if ghandle.rocker(ghandle.up):
        display.show(Image.ARROW_N)
        radio.send('up')
    elif ghandle.rocker(ghandle.down):
        radio.send('down')
        display.show(Image.ARROW_S)
    elif ghandle.rocker(ghandle.left):
        radio.send('left')
        display.show(Image.ARROW_W)
    elif ghandle.rocker(ghandle.right):
        radio.send('right')
        display.show(Image.ARROW_E)
    elif ghandle.rocker(ghandle.noState):
        radio.send('stop')
        display.clear()
    if ghandle.rocker(ghandle.pressed):
        if rocker_key == 0:
            rocker_key = 1
            radio.send('turn_off')
        display.show(Image.NO)
    else:
        rocker_key = 0

    if ghandle.B1_is_pressed():
            radio.send('R')
            display.show("R")
    elif ghandle.B2_is_pressed():
            radio.send('G')
            display.show("G")
    elif ghandle.B3_is_pressed():
            radio.send('B')
            display.show("B")
    elif ghandle.B4_is_pressed():
            radio.send('Y')
            display.show("Y")