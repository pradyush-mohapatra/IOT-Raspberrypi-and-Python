import RPi.GPIO as GPIO
from time import sleep

ledPin = 37
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

myPWM = GPIO.PWM(ledPin, 1000)
myPWM.start(0)

try:
    while(True):
        # Increase brightness from 0% to 100%
        for duty in range(0, 101):
            myPWM.ChangeDutyCycle(duty)
            sleep(0.01) # wait for 0.5 sec after reachng the maximum brightness
            
        sleep(0.5)
        
        for duty in range(100, -1, -1):
            myPWM.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5) # wait for 0.5 sec after reachng the maximum brightness
        
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting Program")

finally:
    myPWM.stop()
    GPIO.cleanup()