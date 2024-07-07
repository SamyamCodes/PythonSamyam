import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
delay = .1
led_pin = 37
inputPin = 40

from time import sleep
GPIO.setup(inputPin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        readVal = GPIO.input(inputPin)
        if readVal ==1:         #This code is for the circuit that is connnecte woth the pin no 1 of 3.3V.
            displayVal = GPIO.output(led_pin, 0)
        if readVal == 0:
            displayVal = GPIO.output(led_pin, 1)        
except KeyboardInterrupt():
    GPIO.cleanup()
    print("That's all Guys.")

# Now, let's write the code for the circuit that is dircetly connected from the push button and the led +ve is also given to GPIO pin 38
import RPi.GPIO as GPIO
from time import sleep
delay = .1
led = 38
inputpin = 40

GPIO.setmode(GPIO.BOARD)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(inputpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # This is done for pull up / down resistor inside the raspberrypi by itself.

try:
    while True:
        readVal = GPIO.input(inputpin, GPIO.IN)
        print(readVal)
        if readVal == 1:
            GPIO.output(led, 0)
        if readVal == 0:
            GPIO.output(led, 1)
        sleep(delay)
except KeyboardInterrupt():  # Interrupt is obtained by Ctrl + C
    GPIO.cleanup()
    print("GPIO ready to Go.")


