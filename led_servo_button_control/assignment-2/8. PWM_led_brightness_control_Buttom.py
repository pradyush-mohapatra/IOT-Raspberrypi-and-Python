import RPi.GPIO as GPIO
from time import sleep

button1 = 40
button2 = 36
ledPin = 37
dutyCycle = 99

# Initial states
LEDState = 0
button1State = 1
button1StateOld = 1
button2State = 1
button2StateOld = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

myPWM = GPIO.PWM(ledPin, 1000)
myPWM.start(dutyCycle)

try:
    while True:
        # Read the current state of the buitton
        button1State = GPIO.input(button1)
        button2State = GPIO.input(button2)
        
        # Check if button1 is pressed
        if button1StateOld == 0 and button1State == 1:
            dutyCycle -= 10
            print("Dim button pressed")
            dutyCycle = max(0, min(dutyCycle, 99))
            print(dutyCycle)
            
        # Check if button2 is pressed
        if button2StateOld == 0 and button2State == 1:
            dutyCycle += 10
            print("Bright button pressed")
            dutyCycle = max(0, min(dutyCycle, 99))
            print(dutyCycle)
            
        #if dutyCycle > 99:
            #dutyCycle = 99
        #if dutyCycle < 0:
            #dutyCycle = 0
        
          #Clamp duty cycle value between 0 and 99
        myPWM.ChangeDutyCycle(dutyCycle)
        
        button1StateOld = button1State
        button2StateOld = button2State
        
        sleep(0.1)
        
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting Program")

finally:
    myPWM.stop()
    GPIO.cleanup()
