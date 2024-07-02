import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 8

GPIO.setwarnings(False) # ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use Physical pin numbering system
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)
try: 
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # Turn on LED
        sleep(0.3)
        GPIO.output(LED_PIN, GPIO.LOW) # Turn off LED
        sleep(0.2)
except:       
    GPIO.cleanup()
