import board
import adafruit_hcsr04
import neopixel
import time
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Kaz.brightness = .3  #setting the brightness of the light, from 0-1 brightness

while True:
    try:
        cm = sonar.distance
        print((sonar.distance))
        time.sleep(0.5)
        if cm < 10:
            Kaz.fill((0, 0, 255))#setting the color with RGB values
        if cm > 10 and cm < 20:
            Kaz.fill((255, 0, 0))#setting the color with RGB values
        else:
            Kaz.fill((0, 255, 0))#setting the color with RGB values
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)