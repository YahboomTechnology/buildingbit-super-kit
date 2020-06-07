from microbit import *
import neopixel

display.show(Image.HAPPY)

np = neopixel.NeoPixel(pin12, 4)
np.clear()
np.show()

while True:
    for num_1 in range(0, 255):
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (num_1, 0, num_1)
            np.show()
            sleep(5)
    for num_2 in range(0, 255):
        for pixel_id in range(0, len(np)):
            np[pixel_id] = (255-num_2, 0, 255-num_2)
            np.show()
            sleep(5)

