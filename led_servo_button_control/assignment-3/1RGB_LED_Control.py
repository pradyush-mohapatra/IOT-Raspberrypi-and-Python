import RPi.GPIO as GPIO
from time import sleep

# Delete pin numbers for RGB LEDs
rPin = 37
gPin = 35
bPin = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

try:
    # Turn on the red LED
    GPIO.output(rPin, 1)
    print("Red LED turned on")
    sleep(5)
    # Turn off the red LED
    GPIO.output(rPin, 0)
    print("Red LED turned off")
    sleep(5)
    
    # Turn on the Green LED
    GPIO.output(gPin, 1)
    print("Green LED turned on")
    sleep(5)
    # Turn off the Green LED
    GPIO.output(gPin, 0)
    print("Green LED turned off")
    sleep(5)
    
    # Turn on the Blue LED
    GPIO.output(bPin, 1)
    print("Blue LED turned on")
    sleep(5)
    # Turn off the Blue LED
    GPIO.output(bPin, 0)
    print("Blue LED turned off")
    sleep(5)
    
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")
finally:
    GPIO.cleanup()