import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
numBlink = int(input("How many Blinks DO you  wish for: "))
for i in range (0, numBlink):
        GPIO.output(11, 1)
        time.sleep(1)
        GPIO.output(11, 0)
        time.sleep(1)
GPIO.cleanup()
