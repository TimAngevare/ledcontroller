import board
import neopixel
from time import sleep
import sys
from numpy import multiply

conditional = True

pixels = neopixel.NeoPixel(board.D18, 240)

color1 = ()

def setcolor(rgb, brightness):
    global color1
    bright = brightness / 100
    color1 = tuple(int(rgb[0] * bright),  int(rgb[1] * bright),  int(rgb[2] * bright))

def fill(): 
    pixels.fill(color1)

def gone():
    print("running")
    conditional = False
    pixels.fill((0,0,0))

def pulse(color1):
    for i in range(10):
        pixels.fill(color1)
        sleep(1.5)
        pixels.fill((0,0,0))
        sleep(1.5)


def slide():
    conditional = True
    while conditional == True:
        x = 239
        while x > 0:
            for i in range(x):
                pixels[i] = color1
                try:
                    pixels[i-1] = color1
                    pixels[i-2] = color1
                except:
                    pass
                sleep(0.001)
                if i >= x-1:
                    pixels[x] = color1
                    pixels[x-1] = color1
                    pixels[x-2] = color1
                    x -= 3
                else:
                    pixels[i] = (0,0,0)
                    pixels[i-1] = (0,0,0)
                    pixels[i-2] = (0,0,0)
        pixels.fill((0,0,0))

