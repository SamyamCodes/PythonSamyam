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
        if readVal ==1:
            displayVal = GPIO.output(led_pin, 0)
        if readVal == 0:
            displayVal = GPIO.output(led_pin, 1)        
except KeyboardInterrupt():
    GPIO.cleanup()
    print("That's all Guys.")

