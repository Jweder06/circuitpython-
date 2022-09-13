import board
import neopixel
import time
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((255, 0, 0))
    print("Red")
    time.sleep(0.5)

    dot.fill((255, 0, 255))
    print("Purple")
    time.sleep(0.5)