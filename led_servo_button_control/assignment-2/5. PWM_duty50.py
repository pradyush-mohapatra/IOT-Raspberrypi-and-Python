import RPi.GPIO as GPIO
from time import sleep

ledPin = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(lenPin, GPIO.OUT)

try:
    myPWM = GPIO.PWM(ledPin, 1000) # Create PWM instance with frequency of 1000
    myPWM.start(50) # Start Pwm with a duty cycle of 50%
    

except KeyboardInterrupt:
    GPIO.cleanup()