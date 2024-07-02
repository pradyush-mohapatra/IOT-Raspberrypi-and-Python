import RPi.GPIO as GPIO
from time import sleep

inPin = 40
outPin = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(outPin, GPIO.OUT)

try:
    while True:       
        readVal = GPIO.input(inPin)
        if readVal == 1:
            GPIO.output(outPin, 0)
        if readVal == 0:
            GPIO.output(outPin, 1)    
        

except KeyboardInterrupt:
    GPIO.cleanup()