import RPi.GPIO as GPIO
from time import sleep

inPin = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

try:
    while True:       
        readVal = GPIO.input(inPin)
        print(readVal)
        sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()