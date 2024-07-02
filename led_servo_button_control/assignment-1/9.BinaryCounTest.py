import RPi.GPIO as GPIO # Import Raspberry Pi GPIO Library
from time import sleep

LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29
ON = 1
OFF = 0

GPIO.setwarnings(False) #IGNORE WARNING FOR NOW
GPIO.setmode(GPIO.BOARD) #USE PHYSICAL NUMBERING SYSTEM
GPIO.setup(LED1, GPIO.OUT, initail= GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initail= GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initail= GPIO.LOW)
GPIO.setup(LED4, GPIO.OUT, initail= GPIO.LOW)
GPIO.setup(LED5, GPIO.OUT, initail= GPIO.LOW)

try:
    GIOP.output(LED1, ON)
    GIOP.output(LED2, ON)
    GIOP.output(LED3, ON)
    GIOP.output(LED4, ON)
    GIOP.output(LED5, ON)
    
except KeyboardInterrupt:
    GPIO.cleanup()