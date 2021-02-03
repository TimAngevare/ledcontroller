import board
import neopixel
from time import sleep
import sys

conditional = True

pixels = neopixel.NeoPixel(board.D18, 240)

color = ()

def setcolor(rgb):
    global color
    color = rgb

def fill(): 
    pixels.fill(color)

def gone():
    print("running")
    conditional = False
    pixels.fill((0,0,0))

def pulse(color):
    for i in range(10):
        pixels.fill(color)
        sleep(1.5)
        pixels.fill((0,0,0))
        sleep(1.5)


def slide():
    conditional = True
    while conditional == True:
        x = 239
        while x > 0:
            for i in range(x):
                pixels[i] = color
                try:
                    pixels[i-1] = color
                    pixels[i-2] = color
                except:
                    pass
                sleep(0.001)
                if i >= x-1:
                    pixels[x] = color
                    pixels[x-1] = color
                    pixels[x-2] = color
                    x -= 3
                else:
                    pixels[i] = (0,0,0)
                    pixels[i-1] = (0,0,0)
                    pixels[i-2] = (0,0,0)
        pixels.fill((0,0,0))
