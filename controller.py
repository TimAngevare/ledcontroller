import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 30)

color = 0

def setcolor(rgb):
    color = rgb

def fill():
    pixels.fill(color)

def slide():
    while True:
        x = 239
        for i in range(x):
            pixels[i].fill(color)
            sleep(0.3)
            if i != x:
                pixels[i].fill((0,0,0))
            x -= 1
        pixels.fill((0,0,0))
