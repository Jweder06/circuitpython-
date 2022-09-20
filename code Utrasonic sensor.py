
import board
import adafruit_hcsr04
import neopixel
import time
import simpleio
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
Dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
Dot.brightness = .3  
while True:
    try:
        cm = sonar.distance
        print((cm))
        x= simpleio.map_range(cm,5,20,255,0)
        y= simpleio.map_range(cm,20,35,0,255)
        z= simpleio.map_range(cm,5,20,0,255)
        time.sleep(0.5)
        if cm < 5:
            Dot.fill((255, 0, 0))
        elif cm < 20:
            Dot.fill((x, 0, z))
        else:
            z= simpleio.map_range(cm,20,35,255,0)
            Dot.fill((0, y, z))
    except RuntimeError:
        print("Retrying!")
        time.sleep(0.1)
    #simpleio.map_range(x, in_min, in_max, out_min, out_max)