import RPi.GPIO as GPIO
from time import sleep

LED_pins=[37,35,33,31,29]

on=1
off=0


GPIO.setwarnings(False) #IGNORE WARNING FOR NOW
GPIO.setmode(GPIO.BOARD) #USE PHYSICAL NUMBERING SYSTEM

for pin in LED_pins:
    GPIO.setup(pin,GPIO.OUT,initial =GPIO.LOW)
    
try:
    for i in range(32):
        for j in range (5):
            GPIO.output(LED_pins[j],(i>>j) & 1)
        sleep(1)
        
   
except KeyboardInterrupt:
    GPIO.cleanup()
