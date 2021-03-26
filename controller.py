import board
import neopixel
from time import sleep
from numpy import subtract, add

conditional = True

pixels = neopixel.NeoPixel(board.D18, 240)

color1 = (0,0,0)

def setcolor(rgb, brightness):
    global color1
    global bright
    bright = brightness / 100
    color1 = (int(rgb[0] * bright),  int(rgb[1] * bright),  int(rgb[2] * bright))

def fill(): 
    pixels.fill(color1)

def gone():
    global conditional
    print("running")
    conditional = False
    pixels.fill((0,0,0))

def pulse(color1):
    for i in range(10):
        pixels.fill(color1)
        sleep(1.5)
        pixels.fill((0,0,0))
        sleep(1.5)

def pulser():
    global conditional
    conditional = True
    global bright
    while conditional == True:
        pixels.fill(color1)
        tempcolor = color1
        newbright = bright
        for x in range(int(bright*99)):
            newbright -= 0.01
            tempcolor = (int(color1[0] * newbright),  int(color1[1] * newbright),  int(color1[2] * newbright))
            pixels.fill(tempcolor)
            sleep(0.07)
        for x in range(int(bright*100)):
            newbright += 0.01
            tempcolor = (int(color1[0] * newbright),  int(color1[1] * newbright),  int(color1[2] * newbright))
            pixels.fill(tempcolor)
            sleep(0.07)
            
def slide():
    global conditional
    conditional = True
    while conditional == True:
        for i in range(239):
            pixels[i] = color1
            for x in range(10):
                pixels[i + x] = (Sint(color1[0] * (bright - x / 10)),  int(color1[1] * (bright - x / 10)),  int(color1[2] * (bright - x / 10)))
                pixels[i - x] = pixels[i + x]
            sleep(0.25)

def stack():
    global conditional
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

