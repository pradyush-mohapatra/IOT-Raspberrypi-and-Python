import RPi.GPIO as GPIO
from time import sleep

# Define pin numbers
inPin = 40
outPin = 38

# Initial States
LEDState = 0 # Initial state of the LED
buttonState=1 #Current state of button switch
buttonStateOld=1 #previos state of button switch

GPIO.setwarnings(False) #Ignre warnings for now
GPIO.setmode(GPIO.BOARD) #Physical numbering system
GPIO.setup(inPin, GPIO.IN, pull_up_down= GPIO.PUD_UP) #use of internal pull up resistors.
GPIO.setup(outPin, GPIO.OUT)

try:
    while True:
        #read the current state of the button
        buttonState= GPIO.input(inPin)
        print(buttonState)
        
        #check if the button state has changed from the present to released.
        if buttonState==1 and buttonStateOld==0:
            #TOGGLE THE STATE OF LED
            LEDState = not LEDState
            # SET THE OUTPUT PIN TO THE NEW LED STATE
            GPIO.output(outPin, LEDState)
            
        #Update the previos button state
        buttonStateOld = buttonState
        
        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
        

            
