# CircuitPython


## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_DistanceSensor](#CircuitPython_DistanceSensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* CircuitPython Motor-Control
* Temperature Sensor
* Rotary Encoder
---

## Hello_CircuitPython

### Description & Code
The purpose of this assignment is to get the serial monitor to print "Hello World"

```python
from time import sleep

while True:
    print("Hello World!") ##Prints "Hello World!" to the serial monitor
    sleep(1)

```


### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/helloworld.gif.gif?raw=true)


Image and code credit goes to paul weder


### Wiring

The wiring of this assignment is quite literally just plugging in the board into one of the USB ports on the Computer

![name](https://github.com/aweder05/CircuitPython/blob/master/media/helloworldwiring.jpg?raw=true)

Image credit goes to [Adafruit Industries](https://www.adafruit.com/product/4000)

### Reflection

The toughest thing about this assignment is getting Visual Studio Code to work with everything. Plus, it's my first time dealing with CircuitPython, and the language is completely different from what I'm used to, which is the Arduino language.




## CircuitPython_Servo

### Description & Code

The purpose of this assignment is to make a servo move using the Adafruit metro board 

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=300)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence

https://user-images.githubusercontent.com/112961442/235830107-5aa59032-f6e4-4af6-ab1f-f41e59bc210d.mp4


### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/spinnerwiring.png?raw=true)
Credit goes to anton weder
### Reflection

This was the firt time that we used a external output with circut python and using circut python to control power running through the arduino.For this assignment I mostly copied their code and wiring while I was still adjusting to using libraries in circut python.

## CircuitPython_DistanceSensor

In this assignment we where tasked with controlling a light on the arduino with a distance sensor where the sensor would swich the light at different distances. We only used a distance sensor for this assignment and the light did not require any wiring.

### Description & Code

```python
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
```

### Evidence

https://user-images.githubusercontent.com/112961442/235830258-77ac981e-e2e6-4537-bb08-402644bfe7b9.mp4



### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/sensorwiring.png?raw=true)

Credit goes to Anton weder

### Reflection

This assignment was relatively simple but I still required help from classmates. Their was some difficulty getting the distance sensor to display the right distances and getting the right libraries to apply. At this point I was still getting used to Circut python and was revcving a lot of help form classmates



## LCD Backpack Button Counter with Toggle Feature


The aim of this assignment was to connect two buttons and an LCD backpack to a breadboard and use them to manipulate a counter displayed on the LCD screen. Pressing one button would increase the counter by one, while pressing the other button while holding down the first one would decrease the counter by one. The count was displayed on the LCD controlled by a backpack.
### Description & Code

```python
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
clickCount = 0

switch = DigitalInOut(board.D3)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27...
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("Jakob")
print("son, i am disapointment.")
while True:
    if not switch.value:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount + 1
            lcd.print(str(clickCount))
        else:
            pass
    else:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount - 1
            lcd.print(str(clickCount))
        else:
            pass
    time.sleep(0.1) # sleep for debounce
```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/lcdbuttontoggle.gif.gif?raw=true)

Credit goes to Anton Weder
### Wiring

![name](https://github.com/aweder05/CircuitPython/blob/master/media/lcdbuttontogglewiring.png?raw=true)

Credit goes to Anton Weder
### Reflection

This assignment was more difficult because it was harder to correctly wire and code the LCD as well as connecting the buttons.

---

## CircuitPython Motor-Control

The purpose of this assignment was to use a Metro Express board to use a potentiometer to determine the speed at which a DC Motor spins. This was accomplished by determining a set range of values at which the DC motor turns on and starts spinning. Then, the more that the potentiometer turns, the faster the motor spins. The motor is being powered by a battery pack, and the potentiometer is powered by the board. 

### Description and Code

```python
import time
import board
import simpleio
from analogio import AnalogIn 
import pwmio  

analog_in = AnalogIn(board.A2) #potentionmeter pin
pin_out = pwmio.PWMOut(board.A1,duty_cycle=65535,frequency=5000)
print("Hello!!")


while True:

    sensor_value = analog_in.value
    # Map the sensor's range from 0<=sensor_value<=255 to 0<=sensor_value<=1023
    mapped_value = int(simpleio.map_range(sensor_value, 0, 65535, 0, 255))

    pin_out.duty_cycle = sensor_value
    print("mapped sensor value: ", sensor_value)
    time.sleep(0.15) 
```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/motorcontrolgif.gif?raw=true)

### Wiring 

![name](https://github.com/lwhitmo/CircuitPython/raw/master/Images/Screenshot%202022-11-01%20115847.png)

### Reflection 

This assignment was very frustrating, but not because the actual assignment was difficult. It was difficult because after switching from one computer to another, everything got messed up, causing a multitude of problems. After fixing all of that, I saw that my wiring was messed up because the diagram I was using was with an Arduino, which powered the potentiometer with 5 volts, when I actually just needed to power it with 3.3. Me not being an expert at wiring, fixing everything and making it work turned out to be a tedious and frustrating process, but in the end, the biggest lesson that I learned from completing this assignment is persistence, and to ask a whole lot of damn questions. 

---

## CircuitPython Temperature Sensor

### Description

To use a Temperature Sensor and LCD Screen to print the current temperature on line 1 of the LCD screen. 
Then on line 2 print a message for the following scenarios: 
    - If the temperature is within a desired range, print a message "It feels great in here"
    - If it is too cold, print "brrr Too Cold!"
    - If it is too hot, print "Too Hot!"
    
### Code

```python
import board
import analogio
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface



# turn on lcd
lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

while lcdPower.value is False:
    print("still sleeping")
    time.sleep(0.1)

time.sleep(1)
print(lcdPower.value)
print("running")

i2c = board.I2C()



lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
TMP36_PIN = board.A0  # Analog input connected to TMP36 output.


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10



# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    lcd.set_cursor_pos(0, 0)
    print("Temperature: {}C {}F".format(temp_C, temp_F))

    lcd.print(("Temperature: {}C {}F".format(temp_C, temp_F)))
    lcd.print((" "))

    time.sleep(1.0)
```

### Evidence

https://user-images.githubusercontent.com/112961442/236002711-28d7d7d1-f7fe-46df-956e-1ce27b852a48.mp4

### Wiring 

![name](https://user-images.githubusercontent.com/112981481/225733918-45b95248-ce2e-4b48-98c1-cc81cd542057.png)

### Reflection
The hardest part about this project was figuring out how to make the LCD screen work. I've gotten it to work in the past, but with the temperature sensor, it's very difficult to get power to the LCD screen and it required additional wiring of a switch to be able to power some LED. I also probably spent a day looking for why my LED wouldn't display and found out that it was because I had the wrong brightness setting.


## Circuit Python Rotary Encoder

### Description 

In this assignment our objective was to create a menu-controlled traffic light using a 20 detent rotary encoder. 

### Code

```python
import rotaryio
import board
import digitalio
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

led: neopixel.Neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1) # initialization of hardware
print("neopixel")

led.brightness = 0.1

button = digitalio.DigitalInOut(board.D12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

colors = [("stop", (255, 0, 0)), ("caution", (128, 128, 0)), ("go", (0, 255, 0))]

encoder = rotaryio.IncrementalEncoder(board.D10, board.D9, 2)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        lcd.clear()
        lcd.print(colors[position % len(colors)][0])
    if(not button.value):
        led[0] = colors[position % len(colors)][1]
    last_position = position
    
Credit for Code goes to Paul Weder

```

### Evidence

![name](https://github.com/aweder05/CircuitPython/blob/master/media/trafficlight.gif)
Gif credits go to River Lewis

### Wiring 

![name](https://github.com/aweder05/CircuitPython/blob/master/media/Screenshot%202023-03-24%20155213.png)
Credit goes to paul weder
### Reflection
This was by far the most difficult assignment and required a lot of help from more experienced coders. I had never used Strings, Arrays, or Constants in my code so it was a challenge to get them to work. Getting everything to work required a lot of guessing and checking and looking waht could went wrong from other errors that other classmates had.
## CircuitPython Photointerrupters

### Description 
Wire up your photointerrupter and have it keep track of how many times it has been interrupted.
Your program outputs the count using a full sentence like "The number of interrupts is: ___" or "I have been interrupted ___ times."
The program outputs the sentence every 4 seconds.

### Code

```python
import time
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import digitalio

lcdPower = digitalio.DigitalInOut(board.D7) #connects the lcd to pin 8
lcdPower.direction = digitalio.Direction.INPUT #sets the lcd power flow as input
lcdPower.pull = digitalio.Pull.DOWN #Pulls the power of the lcd down to ground

while lcdPower.value is False: #creates an infinite loop that repeats until the lcd turns on
    print("zzz")
    time.sleep(0.1)

print("I'm awake")

encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
last_position = 0
btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Buttonyep = 1

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

ledGreen = DigitalInOut(board.D8)
ledYellow = DigitalInOut(board.D9)
ledRed = DigitalInOut(board.D10)
ledGreen.direction = Direction.OUTPUT
ledYellow.direction = Direction.OUTPUT
ledRed.direction = Direction.OUTPUT

while True:
    position = encoder.position
    if position != last_position:
        if position > last_position:
            state = state + 1
        elif position < last_position:
            state = state - 1
        if state > 2:
            state = 2
        if state < 0:
            state = 0
        print(state)
        if state == 0: 
            lcd.set_cursor_pos(0, 0)
            lcd.print("GOOOOO")
        elif state == 1:
            lcd.set_cursor_pos(0, 0)
            lcd.print("yellow")
        elif state == 2:
            lcd.set_cursor_pos(0, 0)
            lcd.print("STOPPP")
    if btn.value == 0 and Buttonyep == 1:
        print("buttion")
        if state == 0: 
                ledGreen.value = True
                ledRed.value = False
                ledYellow.value = False
        elif state == 1:
                ledYellow.value = True
                ledRed.value = False
                ledGreen.value = False
        elif state == 2:
                ledRed.value = True
                ledGreen.value = False
                ledYellow.value = False
        Buttonyep = 0
    if btn.value == 1:
        time.sleep(.1)
        Buttonyep = 1
    last_position = position
    Code credit goes to Grant.G
```

### Evidence
https://user-images.githubusercontent.com/112961442/236007901-c63ca9db-4f76-42a7-afc1-2abdc947ee72.mp4
Credit Grant.G
### Wiring 

### Reflection
This was eaisier than the prevous assignment because it dident include a LCD and only required us to record the Photointerupter individualy
