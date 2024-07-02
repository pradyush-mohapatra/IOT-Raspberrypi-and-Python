import RPi.GPIO as GPIO
from time import sleep

ledPin = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

myPWM = GPIO.PWM(ledPin, 1000) # Create PWM instance with frequency of 1000
try:
    myPWM.start(50) # Start Pwm with a duty cycle of 50%
    sleep(5)
    
    myPWM.start(10) # Start Pwm with a duty cycle of 10%
    sleep(5)
    
    myPWM.start(100) # Start Pwm with a duty cycle of 100%
    sleep(5)
    
    myPWM.start(0) # Start Pwm with a duty cycle of 0%
    sleep(5)
    
    myPWM.ChangeDutyCycle(75) # Start Pwm with a duty cycle of 75%
    sleep(5)
    
except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Exiting Program.")

finally:
    myPWM.stop() # Stop PWM
    GPIO.cleanup()