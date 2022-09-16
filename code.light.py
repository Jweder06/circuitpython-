import board
import neopixel
import time
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2 

print("Make it red!")

while True:
    dot.fill((255, 102, 102))
    print("Red")
    time.sleep(0.5)

    dot.fill((255, 178, 102))
    print("Purple")
    time.sleep(0.5)
        
    dot.fill((255, 255, 102))
    print("Purple")
    time.sleep(0.5)

    dot.fill((178, 255, 102))
    print("Purple")
    time.sleep(0.5)

    dot.fill((102, 255, 102))
    print("Purple")
    time.sleep(0.5)

    dot.fill((102, 255, 178))
    print("Purple")
    time.sleep(0.5)

    dot.fill((102, 255, 255))
    print("Purple")
    time.sleep(0.5)

    dot.fill((102, 178, 255))
    print("Purple")
    time.sleep(0.5)

    dot.fill((102, 102, 255))
    print("Purple")
    time.sleep(0.5)

    dot.fill((178, 102, 255))
    print("Purple")
    time.sleep(0.5)

    dot.fill((255, 102, 255))
    print("Purple")
    time.sleep(0.5)

    dot.fill((255, 102, 178))
    print("Purple")
    time.sleep(0.5)

    dot.fill((192, 192, 192))
    print("Purple")
    time.sleep(0.5)