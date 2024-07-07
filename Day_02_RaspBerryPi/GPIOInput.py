# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD) # This means using pins of raspberryu pi board.
# inPin = 40
# GPIO.setup(inPin, GPIO.IN)
# readVal = GPIO.input(inPin)   # Now, here the pin 40 is connected to pin 1 of 3.3V in Raspberrypi.
# print(readVal) #As a result if gives digital value of 1.

# '''
# Instead of connecting pin 40 with pin 1, if connected with pin 39 (Ground),
# The output in this case would be digital value of 0.
# '''
# GPIO.cleanup()
 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 
inPin = 40
GPIO.setup(inPin, GPIO.IN)

from time import sleep

try:
    while True:

        readVal = GPIO.input(inPin)  
        print(readVal) 
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


 




