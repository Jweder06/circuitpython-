import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D6)
Dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
Dot.brightness = .3

while True:
    try:
        cm = sonar.distance
        simpleio.map_range(cm, 0, 20, 3, 20)
        print((sonar.distance))
        if cm < 7.5:
            r = simpleio.map_range(cm, 0, 6.5, 255, 0)
            g = simpleio.map_range(cm, 5, 7.5, 0, 230)
            Dot.fill((r, g, 0))
        if cm > 7.5 and cm < 12.5:
            g = simpleio.map_range(cm, 7.5, 10, 255, 0)
            b = simpleio.map_range(cm, 9, 12.5, 0, 230)
            Dot.fill((0, g, b))
        if cm > 12.5 and cm < 17.5:
            b = simpleio.map_range(cm, 12.5, 15, 255, 0)
            r = simpleio.map_range(cm, 14, 17.5, 0, 240)
            Dot.fill((r, 0, b))
        time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)