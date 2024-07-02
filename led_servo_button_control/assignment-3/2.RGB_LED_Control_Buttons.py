import RPi.GPIO as GPIO
from time import sleep

# Delete pin numbers for RGB LEDs
rPin = 37
gPin = 35
bPin = 33
rButton = 11
bButton = 13
gButton = 15

# Initial States
rLEDState = 0
gLEDState = 0
bLEDState = 0
rButtonState = 1
rButtonStateOld = 1
gButtonState = 1
gButtonStateOld = 1
bButtonState = 1
bButtonStateOld = 1

# Setup GPIOs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(rButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(gButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(bButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        # Read the current state of the buttons
        rButtonState = GPIO.input(rButton)
        gButtonState = GPIO.input(gButton)
        bButtonState = GPIO.input(bButton)
        print(f"Button States : {rButtonState}, {gButtonState}, {bButtonState}")
        sleep(0.1)
        
        # Check if the button is red button has changed from pressed to released
        if rButtonState == 1 and rButtonStateOld ==0 :
            print("Red colour is activated")
            # Toggle the state of the red LED
            rLEDState = not rLEDState
            # Set the output pin to the new LED state
            GPIO.output(rPin, rLEDState)
            
        if gButtonState == 1 and gButtonStateOld == 0:
            print("Green colour is activated")
            # Toggle the state of the Green LED
            gLEDState = not gLEDState
            # Set the output pin to the new LED state
            GPIO.output(gPin, gLEDState)
            
        if bButtonState == 1 and bButtonStateOld == 0:
            print("Blue colour is activated")
            # Toggle the state of the Blue LED
            bLEDState = not bLEDState
            # Set the output pin to the new LED state
            GPIO.output(bPin, bLEDState)
        
        # Update the previous button states
        rButtonStateOld = rButtonState
        gButtonStateOld = gButtonState
        bButtonStateOld = bButtonState
        
        sleep(0.1)
    
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")
finally:
    GPIO.cleanup()
